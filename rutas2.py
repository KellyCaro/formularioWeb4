import sqlite3 as sql
from flask import Flask,render_template,request,jsonify
from jinja2 import Undefined
from modelo import db,Usuarios
from logging import exception
import logging
from registros.logs import log


loger=log()

DB_PATH="database/base_de_datos.db"
def crearTabla():
    conexion= sql.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE usuarios(
    nombre text,
    correo text,
    ciudad text,
    PRIMARY KEY("correo"))
    """)
    conexion.commit()
    conexion.close()


app=Flask(__name__)         #Creamos una instancia del objeto
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\base_de_datos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)        #tunel entre flask y db



@app.route('/')              #wrap Microservicio, response = lo que retorna
def index():
    return render_template('index.html')     #Respuesta del servidor





@app.route('/consultar')              #wrap Microservicio, response = lo que retorna
def consulta():
        try:
            usuarios=Usuarios.query.all()
            toReturn=[usuario.serialize() for usuario in usuarios]
            return jsonify(toReturn),200

        except Exception:

            Exception("[SERVER]: Error")

            return jsonify({"msg": "Ha ocurrido un error"}),500     #Respuesta del servidor


@app.route('/registrar')              #wrap Microservicio, response = lo que retorna
def reg():
    return render_template('registrar.html')     #Respuesta del servidor


@app.route("/agregar",methods=["POST"])
def addUser():
    try:
        nombre= request.form["nombre"]
        correo= request.form["correo"]
        ciudad= request.form["ciudad"]

        usuario2=Usuarios(nombre,correo,ciudad)

        db.session.add(usuario2)
        db.session.commit()
        loger.registro("e")
        return jsonify(usuario2.serialize()),200
    except Exception:
        Exception("[SERVER]: Error")
        loger.registro("")
        return jsonify({"msg": "Ha ocurrido un error"}),500     #Respuesta del servidor





if __name__== '__main__':
    app.run(debug = True, port =7000)
