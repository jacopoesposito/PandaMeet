from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from flask_login import login_user, current_user, logout_user
from Auth.forms import SignUp, LoginForm
from __init__ import bcrypt, db, login, or_, login_required
from MainApp.routes import mainapp
from models import Users, Paesi, checkEmail, checkUsername
from email_validator import validate_email


auth = Blueprint('Auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('MainApp.index'))
    avaible_countries=Paesi.query.all()
    country_list=[(i.PK_ID_PAESE, i.NOME_PAESE) for i in avaible_countries]
    form = SignUp()
    form.paeseid.choices = country_list
    if form.validate_on_submit():
        if checkEmail(form.mail.data):
            flash('This account already exists!')
            return render_template('register.html', form=form)
        if checkUsername(form.userName.data):
            flash('This username is already taken!')
            return render_template('register.html', form=form)
        else:
            password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = Users(USERNAME=form.userName.data, EMAIL=form.mail.data, PASSWORD=password_hash, SESSO=form.gender.data, DATA_NASCITA=form.dataNascita.data,
                         NAME=form.name.data, FAMILYNAME=form.surname.data, DATE_SIGNUP=datetime.now(), FK_ID_PAESE=form.paeseid.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('MainApp.index'))
    else:
        return render_template('register.html', form=form)
    #return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('MainApp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        if isValid(form.username.data):
            if not checkEmail(form.username.data):
                flash('Password or username not valid')
                return render_template('login.html', form=form)
        else:
            if not checkUsername(form.username.data):
                flash('Password or username not valid!')
                return render_template('login.html', form=form)
        user = Users.query.filter(or_(Users.EMAIL==form.username.data, Users.USERNAME==form.username.data)).first()
        if bcrypt.check_password_hash(user.PASSWORD, form.password.data):
            login_user(user)
            return redirect(url_for('MainApp.index'))
        else:
            flash('Password or username not valid!')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('Auth.login'))


def isValid(email):
    try:
        validate_email(email, check_deliverability=False)
        return True
    except:
        return False