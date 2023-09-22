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

    prompt = "Realiza una evaluación diagnóstica del texto proporcionado, considerando tanto aspectos gramaticales como de estilo. Proporciona una respuesta detallada y precisa que identifique y analice los errores gramaticales y sugerir mejoras para el estilo. En tu respuesta, asegúrate de explicar claramente los errores gramaticales encontrados, proporcionando ejemplos específicos y ofreciendo una revisión precisa de cada uno. Además, sugiere cambios y mejoras para mejorar el estilo del texto, teniendo en cuenta la estructura de las oraciones, la elección de las palabras y la coherencia general."
    
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
