import uuid, os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import current_user
from __init__ import login_required, db
from Users.forms import modifyProfileForm
from models import Users
users = Blueprint('Users', __name__)

@users.route('/profile/<user>', methods=['GET', 'POST'])
@login_required
def profileUsers(user):
    if user != current_user.USERNAME:
        User = Users.get_user(user)
        sex = Users.get_user_sex(User)
        return render_template("user.html", user=User, sex=sex)
    sex = Users.get_user_sex(current_user)
    form = modifyProfileForm()
    if form.validate_on_submit():

        print(form.coverPic.data)
        name = form.name.data
        family_name = form.family_name.data
        bio = form.Biography.data
        cover_pic = form.coverPic.data
        profilePic = form.profilePic.data
        cover_name = str(uuid.uuid4())
        profilepic_name = str(uuid.uuid4())
        cover_pic.save(os.path.join("static/image/users_profile_cover", cover_name))
        profilePic.save(os.path.join("static/image/users_profile_pic", profilepic_name))

        if name and family_name and bio and cover_pic and profilePic:
            return "ciao"


    return render_template("user.html", user=current_user, sex=sex, form=form)






