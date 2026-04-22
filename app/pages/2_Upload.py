import streamlit as st
import pandas as pd
from src.supabase_client import supabase

st.title("📤 Upload de Dados")

uploaded_file = st.file_uploader("Envie seu CSV", type=["csv"])

if uploaded_file is not None:
    try:
        # Ler CSV
        df = pd.read_csv(uploaded_file)

        st.success("Arquivo carregado com sucesso!")

        # Preview
        st.subheader("Pré-visualização")
        st.dataframe(df.head())

        # Botão para enviar
        if st.button("Enviar para o banco"):
            
            data = df.to_dict(orient="records")

            response = supabase.table("vendas_brutas").insert(data).execute()

            st.success("Dados enviados para o banco com sucesso!")

    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")