#Aprendendo Flask-RESTful com python * LoL

from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)  # Instancia o aplicativo Flask
api = Api(app)         # Cria uma API Flask-RESTful


mensagem1 = 'Desenvolver uma API com o Flask-RESTful e seus métodos para um projeto real.'
mensagem2 = 'Desenvolvedor recém promovido a Pleno com diversos projetos em seus repositórios!'
mensagem3 = 'Registro excluido'
mensagem4 = 'Listado as premissas que Desenvolvedor deve possuir ao cargo Senior, fora isso é Pleno ou Junior'

desenvolvedores = [
    {   'id': '1', 
            'nome': 'Albino Pires', 
            'funcao': 'Dev Python Jr', 
            'idade': '41', 
            'tarefa': 'Desenvolver Api com Flask-restful',
            'resumo': mensagem1
           # 'Hard Skill': Habilidades,
    },
    {   'id': '2', 
            'nome': 'Albino Pires', 
            'funcao': 'Dev Python PL', 
            'idade': '41', 
            'tarefa': 'Desenvolver implementações na APIs com diversas ferramentas',
            'Resumo': mensagem2
            #'Hard Skill': lista_habilidades,
    },
]

lista_habilidades = [
    {
        'hard skills': Habilidades,
        'instrucao': mensagem4
    }
]


class Desenvolvedor(Resource):
    
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            menssagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': menssagem}
        except Exception:
            menssagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': menssagem}
        response = desenvolvedores[id]
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        
        # Busca o item pelo ID para atualização
        habilidade_a_atualizar = next((hab for hab in lista_habilidades if hab['id'] == id), None)
        
        if habilidade_a_atualizar:
            habilidade_a_atualizar.update(dados)  # Atualiza os dados sem adicionar novo item
            return habilidade_a_atualizar, 200  # Retorna o item atualizado com status 200 (OK)
        else:
            return {'status': 'erro', 'mensagem': f'Habilidade de ID {id} não existe'}, 404
   
    def delete(self, id):
        
        desenvolvedores.pop(id)
        return({'status':'sucesso', 'mensagem': mensagem3})

class ListaDesenvolvedores(Resource):

    def get(self):
        return desenvolvedores
    
    

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    


api.add_resource(Desenvolvedor, '/dev/<int:id>/')   # Adiciona a rota '/dev/0/' e '/dev/1/' ...
api.add_resource(ListaDesenvolvedores, '/dev/')     # Adiciona a rota '/dev/ listando e atualizando a medida que cresce
api.add_resource(Habilidades, '/habilidades/', '/habilidades/<int:id>/')      # Adiciona a rota /habilidades/' para o módulo da classe Habilidades

if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação Flask

