from flask_login import UserMixin
from __init__ import login, db

@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __table__ = db.Model.metadata.tables['USER']

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.ID_USER)

    def get_user(username):
        User = Users.query.filter_by(USERNAME=username).first()
        return User


class Paesi(db.Model):
    __table__ = db.Model.metadata.tables['PAESI']


class Chat(db.Model):
    __table__ = db.Model.metadata.tables['CHAT']


class Hobby(db.Model):
    __table__ = db.Model.metadata.tables['HOBBY']


class Messaggio(db.Model):
    __table__ = db.Model.metadata.tables['MESSAGGIO']


class PossiedeHobby(db.Model):
    __table__ = db.Model.metadata.tables['POSSIEDE_HOBBY']


def checkEmail(email):
    user = Users.query.filter_by(EMAIL=email).first()

    if user:
        return True
    else:
        return False

def checkUsername(username):
    user = Users.query.filter_by(USERNAME=username).first()

    if user:
        return True
    else:
        return False



