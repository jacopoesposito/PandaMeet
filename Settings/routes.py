from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user

from __init__ import login_required, db

settings = Blueprint('Settings', __name__)

@settings.route('/securitycenter', methods=['GET', 'POST'])
@login_required
def securityCenter():
    return render_template('securitycenter.html')
