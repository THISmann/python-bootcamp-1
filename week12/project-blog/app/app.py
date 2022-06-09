import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    firstName = wtforms.StringField(
        "Name", [wtforms.validators.Length(min=4, max=25), wtforms.validators.DataRequired()])
    lastName = wtforms.PasswordField(
        "Password", [wtforms.validators.Length(min=4, max=25)])
    Message = wtforms.StringField(
        "Bio", [wtforms.validators.Length(min=4, max=25)])
    submit = wtforms.SubmitField("Submit")
