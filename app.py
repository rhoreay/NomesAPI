from flask import Flask
from buscaNome import pegaDadosNome
app = Flask(__name__)


@app.route('/api/<string:nome>/')
def buscaNome(nome):
    response = pegaDadosNome(nome)
    if response == None:
        return ['nome não encontrado']
    else:
        return [nome, response]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=602)

