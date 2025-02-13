import streamlit as st

def main():
    st.set_page_config(page_title="Chatbot de Recetas", page_icon="🍽️", layout="centered")
    st.title("🍽️ Chatbot de Recetas")
    st.write("Bienvenido al chatbot de recetas. Pregunta sobre ingredientes, tiempos de cocción y más.")
    
    # Sección de entrada del usuario
    st.markdown("### 📩 Escribe tu pregunta sobre recetas:")
    user_input = st.text_input("", "Ejemplo: ¿Cómo hacer una pizza casera?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("🍳 Preguntar"):
            response = get_response(user_input)
            st.markdown("### 🤖 Respuesta del Chatbot:")
            st.success(response)
    
    with col2:
        st.image("https://source.unsplash.com/400x300/?cooking,food", caption="Recetas deliciosas", use_column_width=True)
    

def get_response(user_input):
    # Respuestas simuladas (se pueden mejorar con IA o reglas más avanzadas)
    responses = {
        "¿Cómo hacer una pizza casera?": "Para hacer una pizza casera necesitas harina, levadura, agua, sal y tomate. Mezcla los ingredientes, deja reposar la masa, añade los toppings y hornea a 220°C por 15 minutos.",
        "¿Cuánto tiempo se cocina un pollo al horno?": "Depende del peso, pero en promedio un pollo entero se cocina a 180°C por 1 hora y 30 minutos.",
        "¿Qué ingredientes necesito para una torta de chocolate?": "Necesitas harina, cacao en polvo, huevos, leche, azúcar y mantequilla."
    }
    return responses.get(user_input, "Lo siento, no tengo esa información en este momento. Prueba con otra pregunta.")

if __name__ == "__main__":
    main()
