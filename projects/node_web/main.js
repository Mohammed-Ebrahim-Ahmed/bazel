const express = require('express');
const Calculator = require('../node_calculator/calculator');

const app = new express();
const calculator = new Calculator();

app.get('/',(req,res) => {
    res.send(`The result of 10 - 4 = ${calculator.add(10,4)}`);
})

app.listen(8080, () => console.log(`listening on port 8080`));