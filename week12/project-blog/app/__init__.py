import flask

# Remember: __name__ is the name of the file where the code is written
app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
