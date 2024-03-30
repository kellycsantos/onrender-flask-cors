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

app.run(port=5000, host='localhost', debug=True)