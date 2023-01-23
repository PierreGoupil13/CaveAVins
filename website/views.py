from flask import Blueprint, render_template, request, flash, redirect

from website.helpers import check_type, check_num,nom_not_null
from .models import Bouteilles
from .entity import Bottle
from . import db

# Initialise le Blueprint
views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home():
    cave = db.session.query(Bouteilles).all()
    return render_template("home.html", cave=cave)

@views.route('/supprimer/<int:id>', methods=['POST','GET'])
def delete_vin(id):
    # Recuperer les données de quantité de bouteilles, si = 1 alors supprimer, sinon diminuer de 1.
    vin = db.session.query(Bouteilles).filter_by(id=id).first()
    print(vin.nombre)
    if vin.nombre > 1:
        vin.nombre -= 1
        db.session.commit()
        return redirect(f"/single/{vin.id}")
    else:
        db.session.delete(vin)
        db.session.commit()
    
    return redirect("/")

@views.route('/ajouter', methods=['POST', 'GET'])
def ajouter():
    if request.method == 'POST':
        # Get data from form

        # Voir comment utiliser un objet pour recuperer les infos
            # On peut envoyer request.form sous form d'un objet resulat
        bouteille_nouvelle = Bottle( request.form.get('nameBout'), request.form.get('numCaisse'), request.form.get('nombTeil'), request.form.get('comment'), request.form.get('annee'), request.form.get('type'), request.form.get('producteur'), request.form.get('note')
        # nom_vin = request.form.get('nameBout')
        # annee_prod = request.form.get('annee')
        # num_caisse = request.form.get('numCaisse')
        # type_vin = request.form.get('type')
        # producteur = request.form.get('producteur')
        # num_bouteille = request.form.get('nombTeil')
        # note_vin = request.form.get('note')
        # comment = request.form.get('comment')
        # print(request.form)

        # Instaurer du controle sur les infos maintenant
        """ if check_type(type_vin) != True:
            flash("Type de vin incorect, si vous n'êtes pas sur, indiquer autres", category='error') """
        if not(check_num(num_bouteille)):
            flash("Nombre de bouteilles incorrect", category='error')
            return render_template("ajouter.html")
        else:
            num_bouteille = int(num_bouteille)
        
        if not(check_type(type_vin)):
            flash("Type de vin incorect, si vous n'êtes pas sur, indiquer : autres", category='error')
            return render_template("ajouter.html")
        if not(nom_not_null(nom_vin)):
            flash("Nom de vin incorect", category='error')
            return render_template("ajouter.html")

        # Probleme a gerer a ce niveau y'a rien qui marche et ca provoque des pb


        new_bouteille = Bouteilles(
            num_caisse=num_caisse, nombre=num_bouteille, nom_vin=nom_vin, annee=annee_prod, commentaire_vin=comment, note_vin=note_vin,type_vin=type_vin,producteur_vin=producteur
            )
        db.session.add(new_bouteille)
        db.session.commit()
    return render_template("ajouter.html")

@views.route('/single/<int:id>', methods=['POST','GET'])
def single(id):
    vin = db.session.query(Bouteilles).filter_by(id=id).first()
    return render_template("single.html", vin=vin)