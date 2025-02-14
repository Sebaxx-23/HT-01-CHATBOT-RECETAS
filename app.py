import streamlit as st
import random
import requests

def pregunta_aleatoria_placeholder():
    preguntas = [
        "¿Cómo hacer arroz con pollo?",
        "¿Cómo hacer arroz con leche?",
        "¿Qué receta me recomiendas para un lunes?",
        "¿Qué necesito para un manjar blanco?"
    ]
    return random.choice(preguntas)

def get_response(user_input):
    API_KEY = "TU_API_KEY"  # Reemplaza con tu API Key válida
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": user_input}]}]}
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No se pudo generar una respuesta.")
    return "Error en la solicitud a la API."

def get_image(query):
    UNSPLASH_ACCESS_KEY = "TU_UNSPLASH_API_KEY"  # Reemplaza con tu API Key de Unsplash
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("urls", {}).get("regular", "")
    return "https://via.placeholder.com/600"  # Imagen de respaldo

def main():
    st.set_page_config(page_title="Chatbot de Recetas 🍽️", page_icon="🍳", layout="centered")
    
    st.markdown("""
        <style>
            body {background-color: #f4f4f4;}
            .stButton>button {background-color: #ff5733; color: white; font-size: 18px; border-radius: 10px; padding: 10px;}
            .stTextInput>div>div>input {font-size: 18px; padding: 10px; border-radius: 5px;}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""<h1 style='text-align: center; color: #FF5733;'>🍳 Chatbot de Recetas</h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style='text-align: center; color: #4CAF50;'>Tu asistente culinario inteligente</h2>""", unsafe_allow_html=True)
    
    user_input = st.text_input("", pregunta_aleatoria_placeholder(), key="user_input")
    
    if st.button("🔍 Preguntar", help="Haz clic para obtener una receta"):
        response = get_response(user_input)
        image_url = get_image(user_input)
        
        st.markdown("<h3 style='color: #4CAF50;'>🤖 Respuesta del Chatbot:</h3>", unsafe_allow_html=True)
        st.success(response)
        
        st.image(image_url, caption="Imagen relacionada", use_container_width=True)

if __name__ == "__main__":
    main()
