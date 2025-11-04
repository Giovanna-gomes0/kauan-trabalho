# controllers/musicas_controller.py
from flask import jsonify, request
from models.musicas_models import musicas, gerar_id

# POST - Criar música
def criar_musica():
    data = request.json
    if not data:
        return jsonify({"erro": "É necessário enviar dados em JSON"}), 400

    campos = ["titulo", "artista", "genero", "anoLancamento"]
    if not all(campo in data for campo in campos):
        return jsonify({"erro": "Todos os campos são obrigatórios!"}), 400

    nova_musica = {
        "id": gerar_id(),
        "titulo": data["titulo"],
        "artista": data["artista"],
        "genero": data["genero"],
        "anoLancamento": data["anoLancamento"]
    }
    musicas.append(nova_musica)
    return jsonify({"mensagem": "Música cadastrada com sucesso!", "musica": nova_musica}), 201

# GET - Listar todas músicas
def listar_musicas():
    return jsonify(musicas)

# PUT - Atualizar música
def atualizar_musica(id):
    data = request.json
    musica = next((m for m in musicas if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "Música não encontrada!"}), 404

    for campo in ["titulo", "artista", "genero", "anoLancamento"]:
        if campo in data:
            musica[campo] = data[campo]

    return jsonify({"mensagem": "Música atualizada com sucesso!", "musica": musica})

# DELETE - Excluir música
def excluir_musica(id):
    global musicas
    musica = next((m for m in musicas if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "Música não encontrada!"}), 404

    musicas = [m for m in musicas if m["id"] != id]
    return jsonify({"mensagem": "Música excluída com sucesso!"})

# MELHORIA - Buscar por gênero e ordenar por ano
def buscar_por_genero():
    genero = request.args.get("genero")
    if not genero:
        return jsonify({"erro": "Informe um gênero para busca."}), 400

    resultado = [m for m in musicas if genero.lower() in m["genero"].lower()]
    if not resultado:
        return jsonify({"mensagem": "Nenhuma música encontrada nesse gênero."}), 404

    # Ordena por ano de lançamento (melhoria)
    resultado.sort(key=lambda x: x["anoLancamento"])
    return jsonify(resultado)
