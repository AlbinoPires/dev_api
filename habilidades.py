#criando um modulo para implementação na api


from flask_restful import Resource, request
import json

# dev_habilidades.py

# Lista de habilidades
lista_habilidades = [
    {'id': 1, 'habilidade': 'Habilidade em Python'},
    {'id': 2, 'habilidade': 'Habilidade em QA Test'},
    {'id': 3, 'habilidade': 'Habilidade em Java'},
    {'id': 4, 'habilidade': 'Habilidade em PHP'},
    {'id': 5, 'habilidade': 'Orientador, Orquestrador, Desbravador e Coordenador de projetos'}
]

class Habilidades(Resource):
    def get(self, id=None):  # Torna o id opcional
        if id is not None:  # Se um id for passado, busca a habilidade específica
            try:
                return lista_habilidades[id - 1]
            except IndexError:
                return {'status': 'erro', 'mensagem': f'Habilidade de ID {id} não existe'}, 404
        return lista_habilidades  # Se nenhum id, retorna todas as habilidades

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        # Encontra a habilidade com o ID correto
        habilidade_a_deletar = next((hab for hab in lista_habilidades if hab['id'] == id), None)
        
        if habilidade_a_deletar:
            lista_habilidades.remove(habilidade_a_deletar)
            return {'status': 'Deletado com sucesso'}, 200
        else:
            return {'status': 'erro', 'mensagem': f'Habilidade de ID {id} não existe'}, 404
    
    def post(self, id):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)                             # Lê os dados enviados na requisição
        novo_id = max([hab['id'] for hab in lista_habilidades]) + 1  # Gera um novo ID único
        dados['id'] = novo_id                                        # Define o novo ID para a habilidade
        lista_habilidades.append(dados)                              # Adiciona a nova habilidade à lista
        return dados, 201                                            # Retorna a nova habilidade com status 201 (Created)



