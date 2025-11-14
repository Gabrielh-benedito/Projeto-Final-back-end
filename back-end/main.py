from fastapi import FastAPI 
import funcao

app = FastAPI(title="Gerenciador de produtos")

#Criando rota
@app.get("/")
def home():
    return{"Mensagem": "Bem-vindo ao gerenciador de produtos!"}



