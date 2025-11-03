// server.js
const express = require("express");
const app = express();
const musicasRoutes = require("./routes/musicasRoutes");

app.use(express.json());
app.use("/musicas", musicasRoutes);

const PORT = 3000;
app.listen(PORT, () => console.log(`🎵 Servidor rodando na porta ${PORT}`));
