import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Configurar la clave de API de Gemini
API_KEY = "AIzaSyDnQOVbYE2zIs70QX9oK265XkKZhw1WmKc"  # Reemplaza con tu clave real
genai.configure(api_key=API_KEY)

# Crear modelo de texto e imágenes
modelo_texto = genai.GenerativeModel("gemini-1.5-flash")
modelo_imagen = genai.GenerativeModel("gemini-1.5-pro-vision")  # Soporta generación de imágenes

# Interfaz en Streamlit
st.title("🤖 Chatbot IA con Imágenes - Gemini")
st.write("Haz una pregunta y obtén respuesta con imagen.")

# Entrada del usuario
user_input = st.text_input("Tú:", "")

if st.button("Enviar"):
    if user_input:
        with st.spinner("Generando respuesta..."):
            # Generar respuesta de texto
            respuesta = modelo_texto.generate_content([user_input])
            st.text_area("🤖 Gemini:", respuesta.text, height=150)

            # Generar imagen basada en la pregunta
            img_prompt = f"Genera una imagen sobre: {user_input}"
            response_img = modelo_imagen.generate_content([img_prompt])

            # Verificar si la respuesta incluye imágenes
            if response_img and hasattr(response_img, 'text'):
                st.write("📷 Imagen generada por Gemini:")
                for img in response_img.text:  
                    image_data = img.blob  # Obtener los datos binarios de la imagen
                    image = Image.open(io.BytesIO(image_data))
                    st.image(image, caption="Imagen generada por Gemini", use_column_width=True)
    else:
        st.warning("Por favor, escribe algo antes de enviar.")

