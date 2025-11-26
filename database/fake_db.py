# Simulando um banco de dados em memória
produtos_db = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "descricao": "Notebook gamer"},
    {"id": 2, "nome": "Mouse", "preco": 50.00, "descricao": "Mouse sem fio"},
    {"id": 3, "nome": "Teclado", "preco": 120.00, "descricao": None}
]

def get_produtos():
    return produtos_db

def get_produto_por_id(produto_id: int):
    for produto in produtos_db:
        if produto["id"] == produto_id:
            return produto
    return None