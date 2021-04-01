from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
from __init__ import login_required, db
from models import Users

users = Blueprint('Users', __name__)

@users.route('/<user>')
@login_required
def profileUsers(user):
    if user != current_user.USERNAME:
        User = Users.get_user(user)
        return render_template("user.html", user=User)
    return render_template("user.html", user=current_user)
