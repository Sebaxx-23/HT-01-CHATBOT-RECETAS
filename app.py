import streamlit as st
import requests
import json

# PON TU API KEY ENTRE COMILLAS
API_KEY = "AIzaSyDnQOVbYE2zIs70QX9oK265XkKZhw1WmKc"  # Reemplaza con tu clave real

# URL con la API Key incluida
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Función para obtener la respuesta de Gemini
def responder_pregunta(pregunta):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": pregunta}]}]}
    
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        respuesta_json = response.json()
        try:
            return respuesta_json["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "Error al procesar la respuesta de la API."
    else:
        return f"Error {response.status_code}: {response.text}"

# Función para obtener una imagen relacionada usando una API de imágenes
def obtener_imagen(query):
    imagen_url = f"https://source.unsplash.com/600x400/?{query}"  # Usa imágenes aleatorias de Unsplash
    return imagen_url

# Interfaz con Streamlit
st.set_page_config(page_title="Chatbot con IA", layout="centered")
st.title("🤖 Chatbot con Gemini + Imágenes")
st.write("Haz una pregunta y obtén respuestas generadas por la IA, junto con una imagen relacionada.")

# Entrada del usuario
pregunta = st.text_input("✍️ Escribe tu pregunta:")

# Botón para obtener respuesta
if st.button("🔍 Obtener respuesta"):
    if pregunta:
        with st.spinner("Pensando..."):
            respuesta = responder_pregunta(pregunta)
            imagen_url = obtener_imagen(pregunta)
        
        # Mostrar la respuesta
        st.subheader("💬 Respuesta de Gemini:")
        st.write(respuesta)
        
        # Mostrar la imagen relacionada
        st.image(imagen_url, caption="Imagen relacionada", use_column_width=True)
    else:
        st.warning("Por favor, ingresa una pregunta.")
