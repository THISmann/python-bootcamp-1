import flask_wtf
import wtforms


class Login(flask_wtf.FlaskForm):
    username = wtforms.StringField(
        "Name", [wtforms.validators.Length(min=4, max=25), wtforms.validators.DataRequired()])
    password = wtforms.PasswordField(
        "Password", [wtforms.validators.Length(min=4, max=25)])
    submit = wtforms.SubmitField("Submit")
