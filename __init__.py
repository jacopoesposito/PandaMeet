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

    db.init_app(app)        #Init the db
    db.reflect(app=app)     #Reflect the db tables

    #Importing all the blueprints of my app
    from Auth.routes import auth
    from MainApp.routes import mainapp
    from Users.routes import users
    from Users.routes import checkFollower
    from Settings.routes import settings
    from Meet.routes import meet

    app.register_blueprint(auth)      #register the blueprints with the app
    app.register_blueprint(mainapp)
    app.register_blueprint(users)
    app.register_blueprint(settings, url_prefix="/myaccount/")
    app.register_blueprint(meet)
    app.jinja_env.globals.update(checkFollower=checkFollower)

    login.login_view="Auth.login"

    return app
