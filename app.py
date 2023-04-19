from flask import Flask, render_template


app = Flask(__name__)

#LEMBRE-SE -> 
# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa um POST

#É preciso criar rotas que levem em conta as seguintes funcionalidades:
#Listar todos os produtos no template index.html
#Abrir um produto específico (carregando seus dados) no template cadastro.html
#Abrir o template cadastro.html apenas com o id preenchido para permitir novo cadastro
#Dar função aos botões excluir e salvar no template cadastro.html
    


app.run(debug=True)