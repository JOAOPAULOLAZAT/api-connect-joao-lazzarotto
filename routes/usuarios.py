from flask import Blueprint
from controllers.usuarios_controller import (
    listar_usuarios,
    cadastrar_usuario,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario
)

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    return listar_usuarios()


@usuarios_bp.route("/usuarios", methods=["POST"])
def post_usuario():
    return cadastrar_usuario()


@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def get_usuario(id):
    return buscar_usuario(id)


@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def put_usuario(id):
    return atualizar_usuario(id)


@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    return remover_usuario(id)