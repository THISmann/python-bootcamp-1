import flask_wtf
import wtforms


class CreateTask(flask_wtf.FlaskForm):
    name = wtforms.StringField(
        "Name", [wtforms.validators.Length(min=4, max=25), wtforms.validators.DataRequired()])

    executant = wtforms.StringField(
        "Executant", [wtforms.validators.Length(min=4, max=25)])

    date_start = wtforms.StringField(
        "Date_start", [wtforms.validators.Length(min=4, max=25)])

    date_end = wtforms.StringField(
        "Date_end", [wtforms.validators.Length(min=4, max=25)])

    author = wtforms.StringField(
        "Author", [wtforms.validators.Length(min=4, max=25)])

    description = wtforms.StringField(
        "Description", [wtforms.validators.Length(min=4, max=25)])

    status = wtforms.StringField(
        "Status", [wtforms.validators.Length(min=4, max=25)])

    submit = wtforms.SubmitField("Submit")
