from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user

from Settings.forms import passwordChangeForm, usernameChangeForm, emailChangingForm
from __init__ import login_required, db, bcrypt
from models import Users, checkUsername, checkEmail

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
        if emailForm.submitEmail.data and emailForm.validate():
            changeMail(emailForm.newEmail.data)
        if userChangeForm.submit.data and userChangeForm.validate():
            newUsername = userChangeForm.newUsername.data
            if not checkUsername(newUsername):
                current_user.USERNAME = newUsername
                db.session.flush()
                db.session.commit()
                flash(message="Username changed", category='alert-success username-alert')
                return redirect(url_for('Settings.accountInfo', user=current_user.USERNAME))
            else:
                flash(message="Username already taken", category='alert-danger username-alert')
                return render_template('accountinfo.html', userChangeForm=userChangeForm, emailForm=emailForm)
        return render_template('accountinfo.html', userChangeForm=userChangeForm, emailForm=emailForm)
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
