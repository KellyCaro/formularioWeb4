
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class Usuarios(db.Model):
    rowid=db.Column(db.Integer, primary_key= True)
    nombre=db.Column(db.String(200),unique=False,nullable=False)
    correo=db.Column(db.String(80),unique=True,nullable=False)
    ciudad=db.Column(db.String(80),unique=False,nullable=False)

    def __init__(self,nombre,correo,ciudad):
        super().__init__()
        self.nombre=nombre
        self.correo=correo  
        self.ciudad=ciudad
    
    def __str__(self):
        return "Nombre : {}. \nCorreo : {}. \nCiudad : {}.\n".format(self.nombre,self.correo,self.ciudad)

    def serialize(self):
        return{
            "rowid": self.rowid,
            "nombre":self.nombre,
            "correo":self.correo,
            "ciudad":self.ciudad,
            }
        
