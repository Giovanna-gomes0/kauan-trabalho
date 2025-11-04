Listar todas as músicas
GET
/musicas

[
    {
        "id": 1,
        "titulo": "Shape of You",
        "artista": "Ed Sheeran",
        "genero": "Pop",
        "anoLancamento": 2017
    },
    {
        "id": 2,
        "titulo": "Bohemian Rhapsody",
        "artista": "Queen",
        "genero": "Rock",
        "anoLancamento": 1975
    },
    {
        "id": 3,
        "titulo": "Blinding Lights",
        "artista": "The Weeknd",
        "genero": "R&B",
        "anoLancamento": 2019
    }
]

Criar uma nova música
POST
/musicas

{
    "mensagem": "Música cadastrada com sucesso!",
    "musica": {
        "id": 4,
        "titulo": "Levitating",
        "artista": "Dua Lipa",
        "genero": "Pop",
        "anoLancamento": 2020
    }
}

    Atualizar Música    
{
    "mensagem": "Música atualizada com sucesso!",
    "musica": {
        "id": 2,
        "titulo": "Bohemian Rhapsody",
        "artista": "Queen",
        "genero": "Rock",
        "anoLancamento": 1976
    }
}

    Excluir
{
    "mensagem": "Música excluída com sucesso!"
}

    Buscar músicas por gênero (melhoria)
    [
    {
        "id": 1,
        "titulo": "Shape of You",
        "artista": "Ed Sheeran",
        "genero": "Pop",
        "anoLancamento": 2017
    },
    {
        "id": 4,
        "titulo": "Levitating",
        "artista": "Dua Lipa",
        "genero": "Pop",
        "anoLancamento": 2020
    }
]
