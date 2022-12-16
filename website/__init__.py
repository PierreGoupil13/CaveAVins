from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Setup DB
db = SQLAlchemy()
DB_NAME = "vinas.db"

# Code de l'app
def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'randomKey'

    # Creer les BluePrints
    from .views import views
    app.register_blueprint(views, urlprefix='/')

    # # Initialiser la db
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    with app.app_context():
        db.create_all()
        print('Created')

    return app