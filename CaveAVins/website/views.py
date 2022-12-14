from flask import Blueprint, render_template, request, flash
from .models import Bouteilles
from . import db

# Initialise le Blueprint
views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home():
    vin = Bouteilles.query.filter_by(id = 1).first()
    print(vin.nom_vin)
    return render_template("home.html", vin=vin)

@views.route('/ajouter', methods=['POST', 'GET'])
def ajouter():
    if request.method == 'POST':
        # Get data from form
        nom_vin = request.form.get('nameBout')
        annee_prod = request.form.get('annee')
        num_caisse = request.form.get('numCais')

        new_bouteille = Bouteilles(nom_vin = nom_vin, annee=annee_prod, num_caisse=num_caisse)
        db.session.add(new_bouteille)
        db.session.commit()

        print(annee_prod,num_caisse)
    return render_template("ajouter.html")