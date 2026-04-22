import streamlit as st
from src.auth.supabase_auth import sign_in, sign_up

st.title("🔐 Login / Cadastro")

tab1, tab2 = st.tabs(["Login", "Cadastro"])

# ======================
# LOGIN
# ======================
with tab1:
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        try:
            res = sign_in(email, password)
            st.success("Login realizado com sucesso!")
            st.session_state["user"] = res.user
        except Exception as e:
            st.error(f"Erro no login: {e}")

# ======================
# CADASTRO
# ======================
with tab2:
    email_cad = st.text_input("Email cadastro")
    password_cad = st.text_input("Senha cadastro", type="password")

    if st.button("Cadastrar"):
        try:
            sign_up(email_cad, password_cad)
            st.success("Conta criada! Faça login.")
        except Exception as e:
            st.error(f"Erro ao cadastrar: {e}")