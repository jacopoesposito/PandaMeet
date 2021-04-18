from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import Length, Email, EqualTo, NoneOf
from flask_wtf.file import FileAllowed

##Form to modify the personal profile page
class modifyProfileForm(FlaskForm):
    coverPic = FileField('Cover picture', validators=[FileAllowed(['jpeg', 'png', 'jpg'], 'Only images as profile cover')])
    profilePic = FileField('Profile Picture', validators=[FileAllowed(['jpeg', 'png', 'gif'], 'Only images allowed!')])
    name = StringField('Name', validators=[Length(min=1, max=50)])
    family_name = StringField('Family Name', validators=[Length(min=1, max=50)])
    Biography = StringField('Biography', validators=[Length(min=1, max=250, message="Max length for bio of 250 chatacter")])
    submit = SubmitField('Confirm')


