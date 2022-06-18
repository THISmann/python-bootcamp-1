import flask_wtf
import wtforms


class Addtodo(flask_wtf.FlaskForm):
    details = wtforms.StringField(
        "Details", [wtforms.validators.Length(min=4, max=95), wtforms.validators.DataRequired()]) 
    submit = wtforms.SubmitField("Submit")
    