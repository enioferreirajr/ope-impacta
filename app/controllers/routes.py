from app import app
from flask import Flask, render_template, request, redirect, url_for, session

import mysql.connector

app.secret_key = 'segredo'

connection = mysql.connector.connect(host='localhost',
                                         database='ope-impacta',
                                         user='root',
                                         password='1234',
                                         auth_plugin='mysql_native_password')


@app.route('/cadastro_produto/', methods=['GET', 'POST'])
def cadastrar_produto():
    return render_template('cadastroProdutos.html')


@app.route('/criar_produto', methods=['POST', 'GET'])
def criar_produto():
    if request.method == 'POST' and 'descProduto' in request.form and 'marcaProduto' in request.form:
        descProduto = request.form['descProduto']
        marcaProduto = request.form['marcaProduto']
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Produtos (Descricao, Marca) VALUES (%s, %s)', (descProduto, marcaProduto))
            connection.commit()
            msg = 'Cadastro realizado com sucesso!'
            return render_template('cadastroProdutos.html', msg=msg)
        except mysql.connector.Error as err:
            msg = 'Ops! Algo deu errado. Verifique as informações e tente novamente. Erro: {}'.format(err)
            return render_template('cadastroProdutos.html', msg=msg)


@app.route('/CFLogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Usuarios WHERE NomeUsuario = %s AND Senha = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['IdUsuario']
            session['username'] = account['NomeUsuario']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/CFLogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/CFLogin/home', methods=['POST', 'GET'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])

    if request.method == 'GET':
        return redirect(url_for('CFCadastroProduto'))

    # User is not loggedin redirect to login page
    return redirect(url_for('login'))