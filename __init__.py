from flask import Flask, blueprints
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_mail import Mail
from config import DevelopmentConfig
from flask_login import LoginManager, login_required
from flask_bcrypt import Bcrypt

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
login = LoginManager()
bcrypt = Bcrypt()


#This method create the app context


def create_app(confing_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    bootstrap.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    db.init_app(app)
    db.reflect(app=app)

    from Auth.routes import auth
    from MainApp.routes import mainapp

    app.register_blueprint(auth)
    app.register_blueprint(mainapp)

    login.login_view="Auth.login"

    return app
