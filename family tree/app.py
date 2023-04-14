# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Alanna" # escreva seu nome
    idade = "15" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home():

    nome = "Aurélio" # escreva seu nome
    idade = "48" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mae")
def home():

    nome = "Janete" # escreva seu nome
    idade = "49" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.route("/amigo")
def home():

    nome = "Guilherme" # escreva seu nome
    idade = "16" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
