#!/usr/bin/env python
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
	index_random = random.randint(0, len(preguntas) - 1)  # Evitar índice fuera de rango
	return preguntas[index_random]

def main():


	st.set_page_config(page_title="Chatbot de Recetas", page_icon="🍳", layout="centered")
	# Estilo para el título
	st.markdown("<h1 style='text-align: center; color: #FF5733;'>🍳 Chatbot de Recetas</h1>", unsafe_allow_html=True)
	# Estilo para el header
	st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Tu asistente culinario inteligente</h2>", unsafe_allow_html=True)
	# Estilo para la descripción
	st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>Bienvenido al chatbot de recetas. Pregunta sobre ingredientes, tiempos de cocción y más.</p>", unsafe_allow_html=True)
	# Sección de entrada del usuario con estilo mejorado
	st.markdown("<h3 style='color: #FF5733; font-size: 22px;'>📩 Escribe tu pregunta sobre recetas:</h3>", unsafe_allow_html=True)

	def get_response(user_input):

		# Configuración
		API_KEY = "AIzaSyBGdqGYzr40xTMbUS3wfdQuwHU4Bf-AMyg"
		API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

		# Función para hacer la solicitud
		def get_gemini_response(prompt):
			headers = {"Content-Type": "application/json"}
			data = {
				"contents": [{
					"parts": [{"text": prompt}]
				}]
			}

			response = requests.post(API_URL, headers=headers, json=data)
			
			if response.status_code == 200:
				return response.json()
			else:
				return {"error": response.text}

		# Ejemplo de uso
		prompt = user_input
		response = get_gemini_response(prompt)

		# print(response["candidates"][0]["content"]["parts"][0]["text"])

		return response["candidates"][0]["content"]["parts"][0]["text"]


	user_input = st.text_input("", pregunta_aleatoria_placeholder())

	col1, col2 = st.columns([2, 1])

	with col1:
		st.markdown("<h3 style='color: #FF5733;'>🍳 Clickea abajo para obtener una respuesta:</h3>", unsafe_allow_html=True)
		
		if st.button("🔍 Preguntar", help="Haz clic para obtener una receta"):
			response = get_response(user_input)
			st.markdown("<h3 style='color: #4CAF50;'>🤖 Respuesta del Chatbot:</h3>", unsafe_allow_html=True)
			st.success(response)

	with col2:
		st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWIq2c1yUZB6A3SX-FujJCBfA9pxhTViZQ7A&s", caption="Recetas deliciosas", use_column_width=True)


if __name__ == "__main__":
	main()
