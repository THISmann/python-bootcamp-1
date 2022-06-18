import flask
import os
import flask_sqlalchemy
import flask_migrate

# Remember: __name__ is the name of the file where the code is written
app = flask.Flask(__name__)
# Try to avoid hardcoding paths, use os
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
# This line is adding sqlite:/// with the path of your database

app.config['SQLALCHEMY_TRACK_MPDIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
