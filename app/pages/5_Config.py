import streamlit as st

# 🔒 Proteção de acesso
if "user" not in st.session_state:
    st.warning("Você precisa estar logado.")
    st.stop()

st.title("⚙️ Configurações")

st.write("Gerencie suas configurações de conta.")

# Exemplo
st.text_input("Alterar nome (em breve)")
st.text_input("Alterar email (em breve)")

if st.button("Salvar alterações"):
    st.success("Alterações salvas (simulação)")