import openai
import streamlit as st

def assistant():
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        
    st.title("💬 Diagnosticador de español")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key

    prompt = "Analiza la competencia lingüística del autor en un texto dado, evaluando gramática, vocabulario, uso de tiempos verbales, coherencia, cohesión, ortografía y estilo de escritura. Proporciona una evaluación detallada, resaltando fortalezas y áreas de mejora. Utiliza ejemplos del texto para respaldar tus observaciones. Asegúrate de presentar un análisis equilibrado y completo."
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

    user_input = st.text_area("User Input", height=300)

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

    if st.button("Analizar"):
        optimized_prompt = generate_optimized_prompt(prompt)
        st.session_state.messages.append({"role": "user", "content": optimized_prompt})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

def generate_optimized_prompt(prompt):
    # Aquí puedes agregar tu lógica para generar el prompt optimizado
    optimized_prompt = prompt + " [Optimized]"
    return optimized_prompt

assistant()
