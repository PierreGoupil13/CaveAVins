from flask import Blueprint, render_template, request, flash

# Initialise le Blueprint
views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home():

    return render_template("home.html")

@views.route('/ajouter', methods=['POST', 'GET'])
def ajouter():

    return render_template("ajouter.html")