import functools
from flask import Flask, g, render_template, request, flash, redirect, session, url_for, send_file, Response, make_response
from db import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash
import db
import yagmail as yagmail
import utils
import os


app=Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method=='POST':
            username=request.form['username']
            password=request.form['password']
            error= None
            if not username:
                error = "Debe ingersar un usuario"
                flash(error)
                return render_template('login.html')


            if not password:
                error = "Debe ingersar un password"
                flash(error)
                return render_template('login.html')
            db = get_db()
            user = db.execute(
                'SELECT * FROM usuario WHERE usuario=?', (username,)
            ).fetchone()
            if user is None:
                error = "usuario no existe"
            else:
                #validar contraseña here
                store_password = user[4]
                result = check_password_hash(store_password, password)
                if result is False:
                    error='contraseña invalida'
                else:
                    session.clear()
                    session['user_id'] = user[0]
                    resp = make_response(redirect( url_for('send') ) )
                    resp.set_cookie('username', username)
                    return resp
                flash(error)
            return redirect('/home')
        return render_template('login.html')
    except:
        return render_template('login.html')
    
@app.route("/register", methods=["GET", "POST"])
def register():
    try:
        if  request.method == "POST":
            correo=request.form['correo']
            username=request.form['username']
            nombre=request.form['nombre']
            password=request.form['password']
            error=None

            if not utils.isUsernameValid(username):
                error="usuario no valido"
                flash(error)
                #return render_template("register.html")
            
            """if not utils.isPasswordValid(password):
                error="contraseña no valida"
                flash(error)
                #return render_template("register.html")"""
            
            if not utils.isEmailValid(correo):
                error="correo invalido"
                flash(error)
                #return render_template("register.html")
                
            if error is not None:
                return render_template("register.hmtl")    
            else:
                #modificar la siguiente linea con tu informacion personal
                #yag = yagmail.SMTP('wpprueba.prueba0123456@gmail.com', 'prue0123%&/') 
                #yag.send(to=correo, subject='Activa tu cuenta',
                 #   contents='Bienvenido, usa este link para activar tu cuenta ')
                db = get_db()
                db.execute(
                    'INSERT INTO usuario (nombre, usuario, correo, contrasena) VALUES (?,?,?,?)',
                    (nombre, username, correo, generate_password_hash(password))
                )
                db.commit()
                return redirect("/login")    
        else:
            return render_template("register.html")
    except:
        return render_template("register.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cambiar-contraseña")
def ccontra():
    return render_template("ccontraseña.html")

@app.route('/usuarios')
def usuarios():
    db = get_db()
    usuarios = db.execute(
        'SELECT id, Nombre, Usuario, Correo FROM usuario '
    ).fetchall()
    return render_template('usuarios.html', usuarios = usuarios)

app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')#get es para devolver valores de un diccionario 
    print('entro a app.before_request')
    if user_id is None:
        g.user = None
        print('g.user : ',g.user)
    else:#trae una tupla
        g.user = get_db().execute(
            'SELECT id, nombre usuario, correo, contrasena FROM usuario WHERE id = ?',(user_id,)
        ).fetchone

def login_required(view):
    @functools.wrap(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect( url_for('login'))
        return view(**kwargs)
    return wrapped_view


app.route('logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

app.route('/base')
def base():
    return render_template("base.html")