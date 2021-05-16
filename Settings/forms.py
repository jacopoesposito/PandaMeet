from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class passwordChange(FlaskForm):
    oldPassword = PasswordField("Insert old password", validators=[InputRequired])
    newPassword = PasswordField("Insert new password", validators=[InputRequired, Length(min=5, max=15, message="The password must be between 1 and 15")])
    rePassword = PasswordField("Reinsert new password", validators=[InputRequired, Length(min=5, max=20), EqualTo(newPassword, "The Password doesnt match")])
    submit = SubmitField("Confirm")