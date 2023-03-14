from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from backend.db import db
from config import Config
from flask import Flask




def create_app(config_name):
    app= Flask(__name__)
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")



    db.init_app(app)

#importing blue prints
    from backend.users.controller import users
    # regestering blueprints
    app.register_blueprint(users)
    from backend.books.controller import books
    app.register_blueprint(books)








    return app
