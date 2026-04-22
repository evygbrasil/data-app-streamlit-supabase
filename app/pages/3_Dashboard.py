import streamlit as st

if "user" not in st.session_state:
    st.warning("Você precisa estar logado.")
    st.stop()

st.title("📊 Dashboard")
st.write("Você está logado!")