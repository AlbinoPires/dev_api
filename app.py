from flask import Flask, jsonify, request
import json
app = Flask(__name__)


desenvolvedores = [
    {   'id': '0',
        'nome': 'Albino',
    'habilidade':['Python','Flask', 'Django'],
    },
    {   'id': '1',
        'nome': 'Pires',
    'habilidade': ['Python', 'Django']
    }
]


#retorna um desenvolvedor pelo ID e altera / deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])  

def desenvolvedor(id):

    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            menssagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': menssagem}
        except Exception:
            menssagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': menssagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)

        desenvolvedores[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify ({'status': 'sucesso', 'menssagem': 'Registro excluido'})


#listando todos desenvolvedores e inclui um novo desenvolvedor:

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)





if __name__ == '__main__':
    app.run(debug=True)
