import streamlit as st
import requests
import json

# PON TU API KEY ENTRE COMILLAS
API_KEY = "AIzaSyDnQOVbYE2zIs70QX9oK265XkKZhw1WmKc"

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

# Personalización del diseño
st.set_page_config(page_title="ChefBot - Recetas Inteligentes", page_icon="🍽️", layout="centered")
st.markdown("""
    <style>
        .stApp {background-color: #f9f5f0;}
        .title {text-align: center; color: #d35400; font-size: 36px; font-weight: bold;}
        .subtext {text-align: center; color: #555; font-size: 20px; margin-bottom: 20px;}
        .chatbox {background-color: #fff3e6; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);}
        .response {background-color: #fbe5c8; padding: 15px; border-radius: 10px; font-size: 18px; color: #8e44ad;}
    </style>
""", unsafe_allow_html=True)

# Título y descripción
st.markdown("<div class='title'>🍽️ ChefBot - Tu Asistente de Cocina 🍽️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Pregunta sobre recetas, ingredientes y consejos de cocina.</div>", unsafe_allow_html=True)

# Entrada del usuario
txt_placeholder = "Ejemplo: ¿Cómo hago una pasta Alfredo?"
pregunta = st.text_input("Haz tu pregunta sobre cocina o recetas:", placeholder=txt_placeholder)

# Botón para enviar la pregunta
if st.button("🍳 Obtener Receta"):
    if pregunta:
        respuesta = responder_pregunta(pregunta)
        st.markdown(f"<div class='response'>{respuesta}</div>", unsafe_allow_html=True)
    else:
        st.warning("Por favor, ingresa una pregunta.")
