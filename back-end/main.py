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

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    
    if not produtos:
        return {"erro": "Nenhum produto encontrado!"}
    
    lista = []
    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
    
    return {"produtos": lista}


@app.put("/produtos/{id_produto}")
def atualizar_preco(id_produto: int, novo_preco: float):
    produto = funcao.buscar_produto(id_produto)

    if produto:
        funcao.atualizar_preco(id_produto, novo_preco)
        return {"Mensagem": "Preço do produto atualizado com sucesso!"}
    else:
        return {"erro": "produto não encontrado!"}

    
@app.delete("/produtos/{id_produto}")
def deleta_produto(id_produto: int):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.deletar_produto(id_produto)
        return {"mensagem": "produto excluído com sucesso!"}
    return {"erro": "produto não encontrado!"}
