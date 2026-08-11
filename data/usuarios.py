# Lista que simula o banco de dados
usuarios = [
    {
        "id": 1,
        "nome": "Joao Silva",
        "email": "joao@email.com"
    },
    {
        "id": 2,
        "nome": "Maria Souza",
        "email": "maria@email.com"
    }
]

# Proximo ID disponivel
proximo_id = 3


def gerar_id():
    global proximo_id

    novo_id = proximo_id
    proximo_id += 1

    return novo_id