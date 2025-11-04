# routes/musicas_routes.py
from flask import Blueprint
from controllers.musicas_controllers import (
    criar_musica, listar_musicas, atualizar_musica, excluir_musica, buscar_por_genero
)

musicas_bp = Blueprint("musicas_bp", __name__)

musicas_bp.route("/musicas", methods=["POST"])(criar_musica)
musicas_bp.route("/musicas", methods=["GET"])(listar_musicas)
musicas_bp.route("/musicas/<int:id>", methods=["PUT"])(atualizar_musica)
musicas_bp.route("/musicas/<int:id>", methods=["DELETE"])(excluir_musica)
musicas_bp.route("/musicas/filtro", methods=["GET"])(buscar_por_genero)
