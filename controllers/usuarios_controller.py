from flask import jsonify, request
from data.usuarios import usuarios, gerar_id


def listar_usuarios():
    return jsonify(usuarios), 200


def cadastrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Dados nao enviados"
        }), 400

    if not dados.get("nome") or not dados.get("email"):
        return jsonify({
            "error": "Nome e email sao obrigatorios"
        }), 400

    novo_usuario = {
        "id": gerar_id(),
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(novo_usuario)

    return jsonify({
        "data": novo_usuario
    }), 201


def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify(usuario), 200

    return jsonify({
        "erro": "Usuario nao encontrado"
    }), 404


def atualizar_usuario(id):
    dados = request.get_json()

    if not dados or not dados.get("nome") or not dados.get("email"):
        return jsonify({
            "error": "Nome e email sao obrigatorios"
        }), 400

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados["nome"]
            usuario["email"] = dados["email"]

            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "erro": "Usuario nao encontrado"
    }), 404


def remover_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)

            return jsonify({
                "mensagem": "Usuario removido com sucesso"
            }), 200

    return jsonify({
        "erro": "Usuario nao encontrado"
    }), 404