// controllers/musicasController.js
let musicas = require("../models/musicaModel");

// Função auxiliar para gerar ID automático
function gerarId() {
  return Math.floor(Math.random() * 100000);
}

module.exports = {
  // POST - Adicionar uma música
  criarMusica: (req, res) => {
    const { titulo, artista, genero, anoLancamento } = req.body;

    if (!titulo || !artista || !genero || !anoLancamento) {
      return res.status(400).json({ erro: "Todos os campos são obrigatórios!" });
    }

    const novaMusica = {
      id: gerarId(),
      titulo,
      artista,
      genero,
      anoLancamento,
    };

    musicas.push(novaMusica);
    res.status(201).json({ mensagem: "Música cadastrada com sucesso!", musica: novaMusica });
  },

  // GET - Listar todas as músicas
  listarMusicas: (req, res) => {
    res.json(musicas);
  },

  // PUT - Atualizar dados de uma música
  atualizarMusica: (req, res) => {
    const { id } = req.params;
    const { titulo, artista, genero, anoLancamento } = req.body;

    const musica = musicas.find((m) => m.id == id);
    if (!musica) return res.status(404).json({ erro: "Música não encontrada!" });

    if (titulo) musica.titulo = titulo;
    if (artista) musica.artista = artista;
    if (genero) musica.genero = genero;
    if (anoLancamento) musica.anoLancamento = anoLancamento;

    res.json({ mensagem: "Música atualizada com sucesso!", musica });
  },

  // DELETE - Excluir uma música
  excluirMusica: (req, res) => {
    const { id } = req.params;
    const index = musicas.findIndex((m) => m.id == id);

    if (index === -1) return res.status(404).json({ erro: "Música não encontrada!" });

    musicas.splice(index, 1);
    res.json({ mensagem: "Música excluída com sucesso!" });
  },

  // MELHORIA: Buscar músicas por gênero (filtro)
  buscarPorGenero: (req, res) => {
    const { genero } = req.query;
    if (!genero) return res.status(400).json({ erro: "Informe um gênero para busca." });

    const resultado = musicas.filter((m) =>
      m.genero.toLowerCase().includes(genero.toLowerCase())
    );

    if (resultado.length === 0)
      return res.status(404).json({ mensagem: "Nenhuma música encontrada nesse gênero." });

    res.json(resultado);
  },
};
