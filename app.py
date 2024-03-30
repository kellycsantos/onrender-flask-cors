from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


livros = [
    {
        "id": 0,
        "nome" : "Titulo 1",
        "autor" : "Anne"
    },
    {
        "id": 1,
        "nome" : "Titulo 2",
        "autor" : "Sakura"
    },
    {
        "id": 2,
        "nome" : "Titulo 3",
        "autor" : "Solar"
    },
    {
        "id": 3,
        "nome" : "Titulo 4",
        "autor" : "Daya"
    },
]

@app.route('/')
def get_livros():
    return jsonify(livros)


desenhosCartoonNetwork = [
    {
        id: 1,
        nome: "Hora de Aventura",
        anoLancamento: 2010
    },
    {
        id: 2,
        nome: "Steven Universo",
        anoLancamento: 2013
    },
    {
        id: 3,
        nome: "O Incrível Mundo de Gumball",
        anoLancamento: 2011
    },
    {
        id: 4,
        nome: "Apenas um Show",
        anoLancamento: 2010
    },
    {
        id: 5,
        nome: "As Meninas Superpoderosas",
        anoLancamento: 1998
    }
];
@app.route('/desenhos')
def get_desenhos():
    return jsonify(desenhosCartoonNetwork)
