# API Connect

API REST simples para gerenciamento de usuários, desenvolvida como projeto acadêmico.

## Objetivo

A API Connect permite realizar operações básicas de cadastro, consulta, atualização e remoção de usuários.

Cada usuário possui:

- ID
- Nome
- E-mail

Os dados são armazenados temporariamente em memória para simular um banco de dados.

## Tecnologias utilizadas

- Python
- Flask
- JSON
- Git e GitHub
- Thunder Client para testes

## Como executar o projeto

1. Instale o Python.

2. Crie um ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate.bat
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Inicie a aplicação:

```bash
python app.py
```

O servidor será iniciado em:

`http://127.0.0.1:5000`

## Endpoints

| Método | Endpoint | Função |
|---|---|---|
| GET | /usuarios | Lista todos os usuários |
| GET | /usuarios/{id} | Busca um usuário pelo ID |
| POST | /usuarios | Cadastra um novo usuário |
| PUT | /usuarios/{id} | Atualiza um usuário |
| DELETE | /usuarios/{id} | Remove um usuário |

## Exemplo de cadastro

Requisição:

```json
{
  "nome": "Carlos Souza",
  "email": "carlos@email.com"
}
```

Resposta de sucesso:

```json
{
  "data": {
    "id": 3,
    "nome": "Carlos Souza",
    "email": "carlos@email.com"
  }
}
```

Status HTTP: `201 Created`

## Validação

Os campos nome e e-mail são obrigatórios. Caso algum deles não seja informado, a API retorna o status `400 Bad Request`.

Exemplo:

```json
{
  "error": "Nome e email sao obrigatorios"
}
```

Caso seja realizada uma busca por um ID que não existe, a API retorna `404 Not Found`.

```json
{
  "erro": "Usuario nao encontrado"
}
```