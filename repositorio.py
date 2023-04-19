produtos =produtos = {
    1: {
        "nome": "Iphone 14 PRO",
        "descricao": "Iphone 14, modelo PRO MAX, na cor vermelha",
        "preco": 7800.00,
        "imagem": "iphone.jpg"
    },
    2: {
        "nome": "Samsung Galaxy S21",
        "descricao": "Samsung Galaxy S21, modelo com 5G, na cor preta",
        "preco": 5500.00,
        "imagem": "samsung.jpg"
    },
    3: {
        "nome": "MacBook Pro",
        "descricao": "MacBook Pro 16 polegadas, processador M1 Max, na cor prata",
        "preco": 15999.00,
        "imagem": "macbook.jpg"
    },
    4: {
        "nome": "Sony PlayStation 5",
        "descricao": "Console Sony PlayStation 5, com controle DualSense, na cor branca",
        "preco": 4499.00,
        "imagem": "ps5.jpg"
    },
    5: {
        "nome": "Amazon Echo Dot",
        "descricao": "Caixa de som inteligente Amazon Echo Dot, com assistente virtual Alexa, na cor azul",
        "preco": 349.00,
        "imagem": "echo_dot.jpg"
    },
    6: {
        "nome": "Nvidia GeForce RTX 3080",
        "descricao": "Placa de vídeo Nvidia GeForce RTX 3080, 10GB GDDR6X, na cor preta",
        "preco": 7299.00,
        "imagem": "3080.jpg"
    }
}


#id generator
def gerar_id():
    id = max(produtos.keys()) + 1
    return id

#create
def criar_produto(nome:str, descricao:str, preco:float, imagem:str):
    produtos[gerar_id()] = {"nome":nome, "descricao":descricao, "preco":preco, "imagem":imagem}


#update
def atualizar_produto(id:int, dados_produto:dict):
    produtos[id] = dados_produto
    
#delete
def remover_produto(id:int):
    if id in produtos.keys():
        del produtos[id]

#read
def retornar_produto(id:int) -> dict: 
    if id in produtos.keys():
        return produtos[id]
    else:
        return {}

def retornar_produtos() -> dict:
    return produtos



