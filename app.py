import streamlit as st
import google.generativeai as genai

# Configurazione della pagina
st.set_page_config(page_title="Il mio Assistente Gemini", page_icon="🤖")
st.title("🤖 Benvenuto nella mia App")

# --- CONFIGURAZIONE API ---
# Incolla qui la tua chiave API che vedi nella prima immagine
GOOGLE_API_KEY = "AIzaSyCfLI-NKdzv0pfR3gc-UbDFTfi7ZdpDdFQ"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Inizializzazione della cronologia della chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi precedenti
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dell'utente
if prompt := st.chat_input("Chiedimi qualcosa..."):
    # Aggiungi messaggio utente alla cronologia
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Genera risposta dell'assistente
    with st.chat_message("assistant"):
        with st.spinner("Sto pensando..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
