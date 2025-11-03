// routes/musicasRoutes.js
const express = require("express");
const router = express.Router();
const musicasController = require("../controllers/musicasController");

router.post("/", musicasController.criarMusica);
router.get("/", musicasController.listarMusicas);
router.get("/buscar", musicasController.buscarPorGenero); // Melhoria
router.put("/:id", musicasController.atualizarMusica);
router.delete("/:id", musicasController.excluirMusica);

module.exports = router;
