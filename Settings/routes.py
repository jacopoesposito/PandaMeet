from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user

from Settings.forms import passwordChangeForm, usernameChangeForm, emailChangingForm, birthdateChangingForm, countryChangingForm
from __init__ import login_required, db, bcrypt
from models import Paesi, Users, checkUsername, checkEmail

settings = Blueprint('Settings', __name__)


@settings.route('<user>/securitycenter', methods=['GET', 'POST'])
@login_required
def securityCenter(user):
    if user == current_user.USERNAME:
        changePassform = passwordChangeForm()
        if changePassform.validate_on_submit():
            if bcrypt.check_password_hash(current_user.PASSWORD, changePassform.oldPassword.data):
                newPass = bcrypt.generate_password_hash(changePassform.newPassword.data).decode('utf-8')
                current_user.PASSWORD = newPass
                db.session.flush()
                db.session.commit()
                flash(message="Password changed", category='alert-success')
                return render_template('securitycenter.html', changePassform=changePassform)
            else:
                flash(message='The old password is incorrect', category='alert-danger')
                return render_template('securitycenter.html', changePassform=changePassform)
        return render_template('securitycenter.html', changePassform=changePassform)
    return redirect(url_for('MainApp.index'))


@settings.route('<user>/accountinfo', methods=['GET','POST'])
@login_required
def accountInfo(user):
    if user == current_user.USERNAME:
        userChangeForm = usernameChangeForm()
        emailForm = emailChangingForm()
        dateForm = birthdateChangingForm()
        avaible_countries = Paesi.query.all()
        country_list = [(i.PK_ID_PAESE, i.NOME_PAESE) for i in avaible_countries]
        countryForm = countryChangingForm()
        countryForm.paese.choices = country_list
        Country = Paesi.userCountry_by_ID(current_user.FK_ID_PAESE)  #Finding the user country by id, in order to show current country information
        if countryForm.submitCountry.data and countryForm.validate():
            if countryForm.paese.data != current_user.FK_ID_PAESE:
                changeCountry(countryForm.paese.data)
                Country = Paesi.userCountry_by_ID(current_user.FK_ID_PAESE)
            else:
                flash(message="This is already your country", category="alert-warning country-alert")
        if dateForm.submitData.data and dateForm.validate():
            changeBirthdate(dateForm.dataNascita.data)
        if emailForm.submitEmail.data and emailForm.validate():
            changeMail(emailForm.newEmail.data)
        if userChangeForm.submit.data and userChangeForm.validate():
            newUsername = userChangeForm.newUsername.data
            if not checkUsername(newUsername):
                current_user.USERNAME = newUsername
                db.session.flush()
                db.session.commit()
                flash(message="Username changed", category='alert-success username-alert')
                return redirect(url_for('Settings.accountInfo', user=current_user.USERNAME, userCountry=Country))
            else:
                flash(message="Username already taken", category='alert-danger username-alert')
                return render_template('accountinfo.html', userCountry=Country, userChangeForm=userChangeForm, emailForm=emailForm, dateForm=dateForm, countryForm=countryForm)
        return render_template('accountinfo.html', userCountry=Country, userChangeForm=userChangeForm, emailForm=emailForm, dateForm=dateForm, countryForm=countryForm)
    return redirect(url_for('MainApp.index'))

@login_required
def changeMail(email):
    if not checkEmail(email):
        current_user.EMAIL = email
        db.session.flush()
        db.session.commit()
        return flash(message="Email changed!", category="alert-success email-alert")
    else:
        return flash(message="Email already used by another account", category='alert-danger email-alert')


@login_required
def changeBirthdate(date):
    current_user.DATA_NASCITA = date
    db.session.flush()
    db.session.commit()
    return flash(message="Birthdate changed!", category="alert-success date-alert")


@login_required
def changeCountry(country):
    current_user.FK_ID_PAESE = country
    db.session.flush()
    db.session.commit()

    return flash(message="Country changed!", category="alert-success country-alert")



@settings.route('/privatemode', methods=['GET', 'POST'])
@login_required
def enableOrDisablePrivateM():
    if current_user.PRIVATE_MODE == 0:
        current_user.PRIVATE_MODE = 1
        db.session.flush()
        db.session.commit()
    elif current_user.PRIVATE_MODE == 1:
        current_user.PRIVATE_MODE = 0
        db.session.flush()
        db.session.commit()
    return securityCenter()
