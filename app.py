import streamlit as st
import google.generativeai as genai
import os

# Configurar la clave de API de Gemini
API_KEY = "AIzaSyDnQOVbYE2zIs70QX9oK265XkKZhw1WmKc"  # Reemplaza con tu clave real
genai.configure(api_key=API_KEY)

# Función para obtener respuesta de Gemini
def obtener_respuesta(prompt):
    modelo = genai.GenerativeModel("gemini-1.5-flash")  # Puedes usar otro modelo disponible
    respuesta = modelo.generate_content([prompt])
    return respuesta.text

# Interfaz con Streamlit
st.title("🤖 Chatbot IA - Gemini")
st.write("Escribe un mensaje y obtén una respuesta de la IA de Google Gemini.")

# Entrada del usuario
user_input = st.text_input("Tú:", "")

if st.button("Enviar"):
    if user_input:
        with st.spinner("Generando respuesta..."):
            respuesta = obtener_respuesta(user_input)
            st.text_area("🤖 Chatbot:", respuesta, height=150)
    else:
        st.warning("Por favor, escribe algo antes de enviar.")
