import streamlit as st 
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="API", layout="wide")
st.title("Controle de Produtos e Estoque")

menu = st.sidebar.radio("Menu",
    ["Listar Produtos", "Cadastrar Produto", "Excluir Produto", "Atualizar produto", "Valor Total em Estoque"]
    )
if menu == "Listar Produtos":
    st.subheader("Todos os Produtos")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
       produtos = response.json().get("produtos", [])
       if produtos:
           st.dataframe(produtos)
       else:
           st.info("Nenhum produto cadastrado ainda!")
    else:
        st.error("Erro ao tentar conectar com a API.")

elif menu == "Cadastrar Produto":
    st.subheader("➕ Adicionar Produto")
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria do Produto")
    preco = st.number_input("Preço do Produto", min_value=0.0, max_value=2000.00, step=0.5)
    quantidade = st.number_input("Quantidade do Produto", min_value=0.0, max_value=1000.0, step=0.5)
    if st.button("Salvar Produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar produto.")
elif menu == "Excluir Produto":
    st.subheader("Deletar produto")
    id_produto = st.number_input("ID do produto que deseja deletar", min_value=1 , step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/produtos/{id_produto}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data :
                st.success("Produto deletado com sucesso !!")
            else: 
                st.error("Erro ao tentar excluir produto")
        else:
            st.error("Erro ao tentar deletar produto")

elif menu == "Atualizar produto":
    st.subheader("Atualizar preço")
    id_produto = st.number_input("ID do produto a atualizar",
                                 min_value=1, step=1)
    novo_preco = st.number_input("Novo preço", min_value=0.0, step=0.1)

    if st.button("Atualizar"):
        dados = {
            "novo_preco": novo_preco  # <-- nome correto
        }

        # Requisição PUT
        response = requests.put(f"{API_URL}/produtos/{id_produto}",
                                params=dados)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Preço atualizado com sucesso!")
            else:
                st.warning(data["erro"])
        else:
            st.error(f"Erro ao atualizar produto: {response.text}")

elif menu == "Valor Total em Estoque":
    st.subheader("📦 Valor Total do Estoque")

    response = requests.get(f"{API_URL}/produtos")

    if response.status_code == 200:
        produtos = response.json().get("produtos", [])

        if produtos:
            # Calcula o valor total
            valor_total = sum( p["preco"] * p["quantidade"] for p in produtos )

            st.metric(
                label="Valor Total em Estoque",
                value=f"R$ {valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            )

            # Tabela com valor individual
            for p in produtos:
                p["valor_total"] = p["preco"] * p["quantidade"]

            st.dataframe(produtos)

        else:
            st.info("Nenhum produto cadastrado para calcular o estoque.")
    else:
        st.error("Erro ao conectar com a API.")



