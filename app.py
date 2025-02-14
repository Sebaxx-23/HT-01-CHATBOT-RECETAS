import streamlit as st
import requests
import json

# PON TU API KEY ENTRE COMILLAS
API_KEY = "AIzaSyDkvMT-2Tj12K6KAoL7clfVxFVQbAyv79w"  # Reemplaza con tu clave real

# URL con la API Key incluida
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Función para hacer la consulta a Gemini
def responder_pregunta(pregunta):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": pregunta}]}]}
    
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        respuesta_json = response.json()
        try:
            respuesta_texto = respuesta_json["candidates"][0]["content"]["parts"][0]["text"]
            return respuesta_texto
        except (KeyError, IndexError):
            return "Error al procesar la respuesta de la API."
    else:
        return f"Error {response.status_code}: {response.text}"

# Título y descripción
st.title("Chatbot con Gemini")
st.write("Haz una pregunta y obtén respuestas generadas por la IA de Gemini.")

# Entrada del usuario (caja de texto)
pregunta = st.text_input("Escribe tu pregunta:")

# Botón para enviar la pregunta
if st.button("Obtener respuesta"):
    if pregunta:
        respuesta = responder_pregunta(pregunta)
        st.write(f"**Gemini dice:** {respuesta}")
    else:
        st.write("Por favor, ingresa una pregunta.")
