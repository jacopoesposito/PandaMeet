from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user

from Settings.forms import passwordChangeForm
from __init__ import login_required, db, bcrypt
from models import Users

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
    ##if user == current_user.USERNAME:
        return render_template('accountinfo.html')
    ##return redirect(url_for('MainApp.index'))


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
