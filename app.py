import streamlit as st
import pandas as pd
from database import criar_tabela, inserir_funcionario, listar_funcionarios

criar_tabela()

st.set_page_config(page_title="Cadastro de Funcionarios", page_icon="📝")
st.title("Cadastro de Funcionarios")
with st.form("form_funcionario", clear_on_submit=True):
    nome = st.text_input("Nome")
    cargo = st.text_input("Cargo")
    email = st.text_input("email")

    submit= st.form_submit_button("Adicionar")

    if submit:
        if nome and cargo and email:
            try:
                inserir_funcionario(nome, cargo, email)
                st.success(f"Funcionário {nome} adicionado!")
            except Exception as e:
                st.error(f"Erro: {e}")
        else:
            st.warning("Preencha todos os campos!")

st.subheader("Lista de Funcionarios")

dados = listar_funcionarios()
if dados:
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Cargo", "Email"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("Nenhum funcionário cadastrado ainda.")
