import streamlit as st

st.title("Chatbot en Streamlit")
st.write("Escribe tu mensaje y presiona 'Enviar'.")

user_input = st.text_input("Tu mensaje:", "")

if st.button("Enviar"):
    if user_input:
        st.write("Tu mensaje:", user_input)
    else:
        st.warning("Por favor, escribe un mensaje.")
