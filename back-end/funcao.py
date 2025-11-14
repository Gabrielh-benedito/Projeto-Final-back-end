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
        
#criar_tabela() 

def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = connector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
            print("Adicionado com sucesso!!")
        except Exception as erro:
            print(f"Erro ao adicionar o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()  

# nome_produto = input("Digite o nome do produto que deseja adicionar: ")
# categoria_produto = input("Digite a categoria do produto que deseja adicionar: ")
# preco_produto = float(input("Digite o preço do produto: "))
# quantidade_produto = int(input("digite a quantidade do produto: "))
# if __name__ == "__main__":
#     adicionar_produto(nome_produto, categoria_produto, preco_produto, quantidade_produto)

def listar_produtos():
    conexao, cursor = connector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar produtos: {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()


# print(f"Lista de produtos {listar_produtos()}")
# produtos = listar_produtos()
# for i in produtos:
#     print(i)


def atualizar_preco(id_produto, novo_preco):
    conexao, cursor = connector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s WHERE id = %s",
                (novo_preco, id_produto) 
            )
            conexao.commit()
        except Exception as erro:
            print("Erro ao atualizar preço: {erro}")
        finally:
            cursor.close()
            conexao.close()
# id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
# novo_preco = float(input("Adicione novo preço do produto: "))
# atualizar_preco(id_produto, novo_preco)

def delete_produto(id_produto) :
    conexao, cursor = connector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s",
                (id_produto,)
            )
            conexao.commit()
            if cursor.rowcount > 0 :
                print("O filme foi removido com sucesso!")
            else:
                print("Nenhum filme foi econtrado com id fornecido. ")
        except Exception as erro:
            print(f"Erro ao tentar deletar produto: {erro} ")
        finally:
            cursor.close()
            conexao.close()
id_produto = int(input("Digite o ID do produto que deseja deletar: "))
delete_produto(id_produto)