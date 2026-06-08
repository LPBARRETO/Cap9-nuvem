from flask import Flask

# A variável OBRIGATORIAMENTE precisa se chamar "app" para o Azure encontrá-la
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Hello, World! Meu Flask está rodando na Nuvem do Azure!'

if __name__ == '__main__':
    app.run()