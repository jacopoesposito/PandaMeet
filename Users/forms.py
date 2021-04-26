from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from flask_wtf.file import FileAllowed
from wtforms.validators import Length

##Form to modify the personal profile page
class modifyProfileForm(FlaskForm):
    coverPic = FileField('Cover picture', validators=[FileAllowed(['jpeg', 'png', 'jpg'], 'Only images as profile cover')])
    profilePic = FileField('Profile Picture', validators=[FileAllowed(['jpeg', 'png', 'gif'], 'Only images allowed!')])
    name = StringField('Name', validators=[Length(max=50, message="The first name must not exced 50 character")])
    family_name = StringField('Family Name', validators=[Length(max=50, message="The family name must not exced 50 character")])
    Biography = StringField('Biography', validators=[Length(max=250, message="The bio must not exced 250 character")])
    submit = SubmitField('Confirm')


