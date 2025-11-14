# 📦 API de Gerenciamento de Produtos

Este projeto consiste em uma **API desenvolvida com FastAPI**, integrada a um banco de dados PostgreSQL, com um **sistema CRUD completo para gerenciamento de produtos**, e uma **interface gráfica construída em Streamlit** para facilitar o uso.

---

## 🚀 Tecnologias Utilizadas

* **Python**
* **FastAPI** – Criação da API
* **PostgreSQL** – Banco de dados
* **psycopg2** – Conexão com o banco
* **Streamlit** – Interface frontend
* **Requests** – Comunicação entre o frontend e a API
* **dotenv** – Variáveis de ambiente

---

## 🗂 Estrutura do Projeto

### **1. Conexão com o Banco de Dados**

Arquivo responsável por carregar variáveis do ambiente e conectar ao PostgreSQL via psycopg2.

Função principal:

* `connector()` → retorna conexão e cursor.

### **2. Funções CRUD (funcao.py)**

Implementação das operações básicas no banco:

🔹 `criar_tabela()` → Cria tabela `produtos` caso não exista.

🔹 `adicionar_produto(nome, categoria, preco, quantidade)` → Insere novo produto.

🔹 `listar_produtos()` → Lista todos os produtos.

🔹 `atualizar_preco(id_produto, novo_preco)` → Atualiza preço pelo ID.

🔹 `deletar_produto(id_produto)` → Remove produto pelo ID.

🔹 `buscar_produto(id_produto)` → Retorna informações do produto pelo ID.

A estrutura da tabela é:

```sql
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER
);
```

---

## ⚙️ API (FastAPI)

Arquivo principal da API (`main.py`).

### **Rotas disponíveis:**

#### 📌 **GET /**

Retorna mensagem de boas-vindas.

#### 📌 **POST /produtos**

Cadastra um novo produto.
Parâmetros:

* nome (str)
* categoria (str)
* preco (float)
* quantidade (float)

#### 📌 **GET /produtos**

Lista todos os produtos cadastrados.

#### 📌 **PUT /produtos/{id_produto}**

Atualiza o preço de um produto pelo ID.

#### 📌 **DELETE /produtos/{id_produto}**

Remove um produto pelo ID.

---

## 🖥 Interface em Streamlit

Arquivo responsável por criar o painel visual.

### Funcionalidades implementadas:

### ✔ **Listar Produtos**

Exibe os produtos cadastrados em tabela.

### ✔ **Cadastrar Produto**

Formulário para inserir novos itens.

### ✔ **Excluir Produto**

Remove um produto a partir do ID.

### ✔ **Atualizar Produto**

Permite alterar preço.

### ✔ **Valor Total em Estoque**

Exibe um **métrico do valor total** e calcula o total de cada produto.

A interface consome a API via Requests.

---

## ▶️ Como Executar o Projeto

### **1. Clonar o repositório**

```
git clone <seu-repo>
cd projeto
```

### **2. Criar venv (opcional)**

```
python -m venv venv
venv/Scripts/activate
```

### **3. Instalar dependências**

```
pip install -r requirements.txt
```

### **4. Configurar variáveis de ambiente (.env)**

```
DB_NAME=seubanco
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
```

### **5. Iniciar API**

```
uvicorn main:app --reload
```

A API rodará em:

```
http://127.0.0.1:8000
```

### **6. Iniciar interface Streamlit**

```
streamlit run interface.py
```

---

## 📌 Melhorias Futuras

* Adicionar autenticação JWT
* Criar paginação na listagem de produtos
* Implementar categorias dinâmicas via banco
* Adicionar gráficos no Streamlit

---

## 📄 Licença

Projeto livre para estudo.

---


