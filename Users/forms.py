from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from flask_wtf.file import FileAllowed

##Form to modify the personal profile page
class modifyProfileForm(FlaskForm):
    coverPic = FileField('Cover picture', validators=[FileAllowed(['jpeg', 'png', 'jpg'], 'Only images as profile cover')])
    profilePic = FileField('Profile Picture', validators=[FileAllowed(['jpeg', 'png', 'gif'], 'Only images allowed!')])
    name = StringField('Name')
    family_name = StringField('Family Name')
    Biography = StringField('Biography')
    submit = SubmitField('Confirm')


