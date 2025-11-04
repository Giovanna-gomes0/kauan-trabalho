const express = require("express");
const app = express();
const porta = 3000;

app.use(express.json());

const musicasController = require("./controllers/musicasController");

app.post("/musicas", musicasController.criarMusica);
app.get("/musicas", musicasController.listarMusicas);
app.put("/musicas/:id", musicasController.atualizarMusica);
app.delete("/musicas/:id", musicasController.excluirMusica);
app.get("/musicas/filtro", musicasController.buscarPorGenero);

app.listen(porta, () => {
  console.log(`Servidor rodando em http://localhost:{porta}`);
});
