from flask import Flask, request, json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


lista_tarefas = [
    {   'id':0, 
        'responsavel':'José', 
        'tarefa':'Construir app API', 
        'status':'em processo'
    },
    {   'id':1, 
        'responsavel':'William', 
        'tarefa':'Construir front-end', 
        'status':'pausado'
    }
]

class ListaTarefas(Resource):
    def get(self):
        return lista_tarefas

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_tarefas)
        dados['id'] = posicao
        lista_tarefas.append(dados)
        return lista_tarefas[posicao]



class Tarefa(Resource):
    def get(self, id):
        try:
            response = lista_tarefas[id]
        except IndexError:
            mensagem = "Tarefa com ID {} não existe!".format(id)
            response = {"status": "erro", "mensagem": mensagem }
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API!"
            response = {"status": "erro", "mensagem": mensagem }
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_tarefas[id] = dados
        return dados
    
    def delete(self, id):
        lista_tarefas.pop(id)
        return {'status':'Sucesso', 'mensagem':'Registro excluído'}


api.add_resource(ListaTarefas, "/tarefas")
api.add_resource(Tarefa,"/tarefas/<int:id>")


if __name__=='__main__':
    app.run()
