const express = require('express');
const router = express.Router();

// Ruta de prueba
router.get('/', (req, res) => {
  res.json({ message: 'Bienvenido al servidor Express' });
});

module.exports = router;
