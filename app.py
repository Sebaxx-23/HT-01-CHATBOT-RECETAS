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
            return "❌ Error al procesar la respuesta de la API."
    else:
        return f"⚠️ Error {response.status_code}: {response.text}"

# Configuración de estilos CSS
st.markdown("""
    <style>
        body { background-color: #000000; }
        .stApp { background-color: #000000; color: #ffffff; }
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #ffcc00; }
        .description { text-align: center; font-size: 18px; color: #aaaaaa; margin-bottom: 20px; }
        .chatbox { background-color: #222222; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1); }
        .response { background-color: #444444; padding: 15px; border-radius: 10px; font-size: 18px; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# Título con emojis
st.markdown("<div class='title'>🤖 ChefBot - Tu Asistente de Cocina IA🔥</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>💬 Haz una pregunta y obtén respuestas paso a paso.</div>", unsafe_allow_html=True)

# Entrada del usuario con placeholder
pregunta = st.text_input("✍️ Escribe tu pregunta aquí:", placeholder="Ejemplo: ¿Cómo hago una pasta Alfredo? 🍝")

# Botón con icono
if st.button("🚀 Obtener Respuesta"):
    if pregunta:
        respuesta = responder_pregunta(pregunta)
        st.markdown(f"<div class='response'>💡 <b>Gemini dice:</b><br>{respuesta}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Por favor, ingresa una pregunta.")
