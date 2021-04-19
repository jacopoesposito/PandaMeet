import uuid, os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
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
    if form.is_submitted():

        print(form.coverPic.data)
        name = form.name.data
        family_name = form.family_name.data
        bio = form.Biography.data
        if form.coverPic.data.filename != '':
            cover_pic = form.coverPic.data
            cover_name = str(uuid.uuid4())
            profile_cover_link = os.path.join("static/image/users_profile_cover", cover_name)
            cover_pic.save(profile_cover_link)
            current_user.PROFILE_COVER = "/" + profile_cover_link
        if form.profilePic.data.filename != '':
            profilePic = form.profilePic.data
            profilepic_name = str(uuid.uuid4())
            profile_pic_link = os.path.join("static/image/users_profile_pic", profilepic_name)
            profilePic.save(profile_pic_link)
            current_user.PROFILE_PIC = "/" + profile_pic_link

        if name:
            current_user.NAME = name
        if family_name:
            current_user.FAMILYNAME = family_name
        if bio:
            current_user.BIOGRAFIA = bio

        db.session.flush()
        db.session.commit()

    return render_template("user.html", user=current_user, sex=sex, form=form)






