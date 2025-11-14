import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Produtos", layout="wide")
st.title("Gerenciador de produtos")

menu = st.sidebar.radio("Menu", 
                 ["Listar produto", "Cadastrar produto","Deletar produto","Atualizar preco"]
                 )
if menu == "Listar produto":
    st.subheader("Todos os produtos")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos",[])
        if produtos:
            st.dataframe(produtos)
        else:
            st.error("erro ao conectar com a API")
    else:
        st.error("erro ao conectar com a API.") 
elif menu == "Cadastrar produto":
    st.subheader("➕ Adicionar produto")
    titulo = st.text_input("Nome do produto")
    genero = st.text_input("" \
    "")
    ano = st.number_input("Ano de Lançamento do Filme", min_value=1900, max_value= 2100, step=1)
    nota = st.number_input("Nota do filme (0 a 10)", min_value=0.0, max_value= 10.0, step=0.5)
    if st.button("Salvar filme"):
        dados ={"titulo": titulo, "genero": genero, "ano": ano, "nota": nota}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesso!")
        else:
            st.error("erro ao adicionar filme. ")
elif menu == "Deletar Filme":
    st.subheader("🗑 Deletar Filme")
    id_filme = st.number_input("Id do filme a excluir", min_value=1, step=1)
    if st.button("Excluir "):
        response =  requests.delete(f"{API_URL}/filmes/{id_filme}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Filme excluido com sucesso !")
            else:
                st.error("Erro ao tentar excluir filme!")
        else:
            st.error("erro ao excluir o filme")

elif menu == "Atualizar Filme":
    st.subheader("Atualizar Filme")
    id_filme = st.number_input("ID do filme a atualizar", min_value=1,step=1)
    nota = st.number_input("Nova nota", min_value=0.0, max_value=10.0, step=0.5)
    if st.button("Atualizar"):
        dados = {
            "id_filme"
            "nova_nota"
        }
        response = requests.put(f"{API_URL}/filmes/{id_filme}", params=dados)
        if response.status_cod == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Filme atualizado com sucesso!")
            else:
                st.warning(data["erro"])
        else:
            st.error("Erro ao atualizar filme.")
