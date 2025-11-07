from conexao import connector

def criar_tabela():
    conexao, cursor = connector()
    if conexao:
        try:
            cursor.execute("""
               CREATE TABLE IF NOT EXISTS produtos (
               id SERIAL PRIMARY KEY,
               nome TEXT NOT NULL,
               categoria TEXT NOT NULL,
               preco REAL NOT NULL,
               quantidade INTEGER
                )
            """)
            conexao.commit()
            print("Tabela Criada !!")
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()
        

