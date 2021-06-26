from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, DateField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo, Email, NoneOf


class passwordChangeForm(FlaskForm):
    oldPassword = PasswordField("Insert old password", validators=[InputRequired()])
    newPassword = PasswordField("Insert new password", validators=[InputRequired(), Length(min=5, max=15, message="The password must be between 1 and 15")])
    rePassword = PasswordField("Confirm", validators=[InputRequired(), Length(min=5, max=15, message=""), EqualTo('newPassword', message="The Password doesnt match")])
    submit = SubmitField("Confirm")


class usernameChangeForm(FlaskForm):
    newUsername = StringField("Insert your new username", validators=[InputRequired(), Length(min=5, max=20, message="Username must be "
                    "between 5 and 20 character"), NoneOf("@", message="Dont use @")])
    submit = SubmitField("Confirm")


class emailChangingForm(FlaskForm):
    newEmail = StringField('Email', validators=[InputRequired(), Email("Please write your email")])
    submitEmail = SubmitField("Confirm")

class birthdateChangingForm(FlaskForm):
    dataNascita = DateField('Data di nascita', validators=[InputRequired("Insert your date of birth")], format="%Y-%m-%d")
    submitData = SubmitField("Confirm")


class countryChangingForm(FlaskForm):
    paese = SelectField(u'Country', coerce=int, validators=[InputRequired()])
    submitCountry = SubmitField("Confirm")


class setHobbiesForm(FlaskForm):
    hobby = SelectField(u'Hobby', coerce=int, validators=[InputRequired()])
    submitHobby = SubmitField("Confirm")
