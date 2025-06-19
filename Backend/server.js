const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.static('../frontend'));

app.get('/', (req, res) => {
    res.send('Node main.py is up');
});

app.listen(port, () => {
    console.log('Server running on http://localhost:${port}');
})