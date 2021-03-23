from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo, NoneOf
from __init__ import db



class SignUp(FlaskForm):
    userName = StringField('Username', validators=[InputRequired("Insert your username"), Length(min=5, max=20), NoneOf("@", message="Dont use @")])
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=50)])
    surname = StringField('Surname', validators=[InputRequired(), Length(min=1, max=50)])
    gender = SelectField(u'Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    dataNascita = DateField('Data di nascita', validators=[InputRequired("Insert your date of birth")], format="%Y-%m-%d")
    paeseid = SelectField(u'Country', coerce=int, validators=[InputRequired()])
    mail = StringField('Email', validators=[InputRequired(), Email("Please write your email")])
    password = PasswordField('Password', validators=[InputRequired(),
                                                     Length(min=5, max=15, message="Password must be between 5 and 15 character long")])
    rePassword = PasswordField('Password', validators=[InputRequired(), EqualTo('password', message='Password dont match')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign in')


