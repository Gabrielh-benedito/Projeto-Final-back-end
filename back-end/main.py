from fastapi import FastAPI 
import funcao

app = FastAPI(title="Gerenciador de produtos")

#Criando rota
@app.get("/")
def home():
    return{"Mensagem": "Bem-vindo ao gerenciador de produtos!"}

@app.post("/produtos")
def cadastrar_produtos(nome: str, categoria: str, preco: float, quantidade: float):
    funcao.adicionar_produto(nome, categoria, preco, quantidade)
    return{"200": "Produto cadastrado com sucesso!"}


