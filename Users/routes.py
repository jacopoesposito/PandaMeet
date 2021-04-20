import uuid, os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from flask_login import current_user
from datetime import datetime
from __init__ import login_required, db
from Users.forms import modifyProfileForm
from models import Users, Follow
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
        if form.coverPic.data.filename != '': #Check if the users uploaded a new cover picture
            cover_pic = form.coverPic.data
            cover_name = str(uuid.uuid4())
            profile_cover_link = os.path.join("static/image/users_profile_cover", cover_name)
            cover_pic.save(profile_cover_link)
            current_user.PROFILE_COVER = "/" + profile_cover_link
        if form.profilePic.data.filename != '': #Check if the users uploaded a new profile pic
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


@users.route('/follow/<userToFollow>', methods=['GET', 'POST'])
@login_required
def followUser(userToFollow):
    user = Users.get_user(userToFollow)
    if user.ID_USER != current_user.ID_USER:
        if not checkFollower(user):
            follow = Follow(ID_USER_1=current_user.ID_USER, FOLLOWER=user.ID_USER, DATA_FOLLOW=datetime.now())
            db.session.add(follow)
            db.session.commit()
            return profileUsers(userToFollow)
        return profileUsers(userToFollow)


@users.route('/unfollow/<userToUnfollow>', methods=['GET', 'POST'])
@login_required
def unfollowUser(userToUnfollow):
    user = Users.get_user(userToUnfollow)
    if user.ID_USER != current_user.ID_USER:
        if checkFollower(user):
            Follow.query.filter(Follow.ID_USER_1==current_user.ID_USER, Follow.FOLLOWER==user.ID_USER).delete()
            db.session.commit()
            return profileUsers(userToUnfollow)
    return profileUsers(userToUnfollow)


def checkFollower(user):
    follower = Follow.query.filter(Follow.ID_USER_1==current_user.ID_USER, Follow.FOLLOWER==user.ID_USER).first()

    if follower:
        return True
    else:
        return False



