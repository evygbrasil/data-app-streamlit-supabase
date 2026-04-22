import streamlit as st

# 🔒 Proteção de acesso
if "user" not in st.session_state:
    st.warning("Você precisa estar logado.")
    st.stop()

st.title("💳 Meu Plano")

st.write("Aqui você poderá visualizar seu plano atual.")

# Exemplo simples
st.info("Plano atual: Gratuito")

st.button("Fazer upgrade (em breve)")