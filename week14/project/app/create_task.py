import flask_wtf
import wtforms


class CreateTask(flask_wtf.FlaskForm):
    name = wtforms.StringField(
        "Name", [wtforms.validators.Length(min=4, max=25), wtforms.validators.DataRequired()])

    executant = wtforms.StringField(
        "Executant", [wtforms.validators.Length(min=4, max=25)])

    date_start = wtforms.DateField(
        "Date_start")

    date_end = wtforms.DateField(
        "Date_end")

    author = wtforms.StringField(
        "Author", [wtforms.validators.Length(min=4, max=25)])

    description = wtforms.StringField(
        "Description", [wtforms.validators.Length(min=4, max=25)])

    status = wtforms.StringField(
        "Status", [wtforms.validators.Length(min=4, max=25)])

    submit = wtforms.SubmitField("Submit")
