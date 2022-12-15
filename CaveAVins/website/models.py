from . import db
from sqlalchemy.sql import func

class Bouteilles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_caisse = db.Column(db.Integer, unique=True)
    nombre = db.Column(db.Integer)
    nom_vin = db.Column(db.String(100))
    annee = db.Column(db.Integer)
    commentaire_vin = db.Column(db.String(1000))
    note_vin = db.Column(db.Integer)
    type_vin = db.Column(db.String(20))
    producteur_vin = db.Column(db.String(50))
    date = db.Column(db.DateTime(timezone=True), default = func.now())



