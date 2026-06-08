from flask import Flask, jsonify, request

app = Flask(__name__)

# ==========================================
# EXERCÍCIO 9.3 - A Rota Hello World
# ==========================================
@app.route('/')
def hello_cloud():
    return 'Hello, World! Meu Flask está rodando na Nuvem do Azure!'

# ==========================================
# EXERCÍCIO 9.4 - A Rota da API RESTful
# ==========================================
tarefas = [
    {"id": 1, "titulo": "Finalizar o Capítulo 9", "concluida": False}
]

@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    return jsonify(tarefas), 200

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    nova_tarefa = request.get_json()
    tarefas.append(nova_tarefa)
    return jsonify({"mensagem": "Tarefa criada com sucesso!", "tarefa": nova_tarefa}), 201

if __name__ == '__main__':
    app.run()