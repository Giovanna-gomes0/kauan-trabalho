# models/musica_model.py

# "Banco de dados" em memória
musicas = [
    {"id": 1, "titulo": "Shape of You", "artista": "Ed Sheeran", "genero": "Pop", "anoLancamento": 2017},
    {"id": 2, "titulo": "Bohemian Rhapsody", "artista": "Queen", "genero": "Rock", "anoLancamento": 1975},
    {"id": 3, "titulo": "Blinding Lights", "artista": "The Weeknd", "genero": "R&B", "anoLancamento": 2019},
]

def gerar_id():
    return max([m["id"] for m in musicas], default=0) + 1
