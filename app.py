import streamlit as st
from openai import OpenAI

Client = OpenAI(api_key = st.secrets.OpenAIAPI.openai_api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
    {"role": "system", "content": "Piensa como tripadvisor."}
]

def comunicate():
  messages = st.session_state["messages"]
  user_messages = {"role": "user", "content": st.session_state["user_input"]}
  messages.append(user_messages)
  response = Client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)
  bot_messages = response.choices[0].message
  messages.append(bot_messages)

st.session_state["user_input"] = ""

#user interface

st.title ("tripadvisor AI")
st.write ("Utilizando la API chatGPT, este chatbot ofrece capacidades conversacionales avanzadas.")

user_input = st.text_input("por favor ingrese un mensaje aquí.", key="user_input", on_change=comunicate)

if st.session_state["messages"]:
  messages = st.session_state["messages"]

  for msg in reversed(messages[1:]):
    if isinstance(msg, dict):
        speaker = "💀" if msg["role"] == "user" else "🤢"
        st.write(speaker + ": " + msg["content"])
    else:
        st.write("😂: " + msg.content)

def main():
  sidebar = st.siderbar
  page = sidebar.radio("seleccione chatbot", ["Trip Adviser", "Business Adviser"])

  if page == "Arip Adviser"
