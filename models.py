from flask_login import UserMixin
from sqlalchemy import and_

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

    def get_user_sex(User):
        if(User.SESSO == 'M'):
            return 'Male'
        if(User.SESSO == 'F'):
            return 'Female'
        if(User.SESSO == 'O'):
            return 'other'


class Paesi(db.Model):
    __table__ = db.Model.metadata.tables['PAESI']

    def userCountry_by_ID(countryID):
        Country = Paesi.query.filter_by(PK_ID_PAESE = countryID).first()
        return Country


class Chat(db.Model):
    __table__ = db.Model.metadata.tables['CHAT']


class Hobby(db.Model):
    __table__ = db.Model.metadata.tables['HOBBY']

    def returnHobbiesByOwnerID(id_user):
        Hobbies = Hobby.query.with_entities(Hobby.PK_ID_HOBBY
        , Hobby.NOME_HOBBY).join(PossiedeHobby, Hobby.PK_ID_HOBBY==PossiedeHobby.FK_ID_HOBBY).join(Users, PossiedeHobby.FK_ID_UTENTE==Users.ID_USER)\
            .filter_by(ID_USER=id_user).all()
        return Hobbies

    def checkOwnedHobbies(id_hobby, id_users):
        Hobbies = Hobby.query.with_entities(Hobby.PK_ID_HOBBY).join(PossiedeHobby, Hobby.PK_ID_HOBBY==PossiedeHobby.FK_ID_HOBBY).\
            join(Users, PossiedeHobby.FK_ID_UTENTE==Users.ID_USER).filter(and_(Users.ID_USER==id_users, Hobby.PK_ID_HOBBY==id_hobby)).first()

        if Hobbies:
            return True
        else:
            return False


class Messaggio(db.Model):
    __table__ = db.Model.metadata.tables['MESSAGGIO']


class PossiedeHobby(db.Model):
    __table__ = db.Model.metadata.tables['POSSIEDE_HOBBY']


class Follow(db.Model):
    __table__ = db.Model.metadata.tables['FOLLOW']


class Domanda(db.Model):
    __table__ = db.Model.metadata.tables['DOMANDA']


class Risposta(db.Model):
    __table__ = db.Model.metadata.tables['RISPOSTA']


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

def returnHobbies():
        Hobbies = Hobby.query.filter_by(APPROVATO = 1).all()
        return Hobbies


