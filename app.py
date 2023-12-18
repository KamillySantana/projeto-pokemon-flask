#pasta static, serve para armezanar imgs, css e java script
#pasta templatess, armazenar html

#metodos http sao usados para definir a ação que se deja realizar no servidor, GET, POST, PUT, DELETE
#rota intermediaria nao tem html

from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__) #criação de obj usando class Flask
app.secret_key = 'Senai'

class cadpokemon:
    def __init__(self, numero, nome, tipo, altura, peso):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso

lista = []

@app.route('/pokemon')
def pokemon():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Pokemon.html', Titulo = "Pokémons", ListaPokemons = lista)

@app.route('/cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Cadastro.html', Titulo = "Cadastro de Pokemon")

@app.route('/criar', methods=['POST']) #rota inter
def criar():
    if 'salvar' in request.form:
        numero = request.form['numero']
        nome = request.form['nome']
        tipo = request.form['tipo']
        altura = request.form['altura']
        peso = request.form['peso']
        obj = cadpokemon(numero,nome,tipo,altura,peso)
        lista.append(obj)
        return redirect('/pokemon')
    elif 'deslogar' in request.form:
        return redirect('/')

@app.route('/excluir/<numeropkm>', methods=['GET', 'DELETE']) #rota inter
def excluir(numeropkm):
    for i, pkm in enumerate(lista):
        if pkm.numero == numeropkm:
            lista.pop(i)
            break
    return redirect('/pokemon')

@app.route('/editar/<numeropkm>', methods=['GET'])
def editar(numeropkm):
    for i, pkm in enumerate(lista):
        if pkm.numero == numeropkm:
            return render_template('Editar.html', pokemon=pkm, Titulo='Alterar Pokemon')

@app.route('/alterar', methods = ['POST', 'PUT']) #rota inter
def alterar():
    numero = request.form['numero']
    for i, pkm in enumerate(lista):
        if pkm.numero == numero:
            pkm.nome = request.form['nome']
            pkm.tipo = request.form['tipo']
            pkm.altura = request.form['altura']
            pkm.peso = request.form['peso']
    return redirect('/pokemon')

@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', Titulo='Faça seu login')

@app.route('/autenticar', methods=['POST']) #rota inter
def autenticar():
    if request.form['usuario'] == 'kamilly' and request.form['senha'] == '123':
        session['Usuario_Logado'] = request.form['usuario']
        flash('Usuario logado com sucesso')
        return redirect('/cadastro')
    else:
        flash('Usuario não encontrado')
        return redirect('/')

if __name__ == '__main__': #testa para ver c esta rodando em outro computadores
    app.run()

#=======================

#@app.route('/') #cria uma rota, / é apenas o endereço, coloca / e o que eu quero acessar
#def hello_world(): #A rota sempre espera uma função
    #return 'Hello World!'

