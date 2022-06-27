import flask
import os
import flask_sqlalchemy
import flask_migrate
from flask_login import LoginManager

# Remember: __name__ is the name of the file where the code is written
app = flask.Flask(__name__)
# Try to avoid hardcoding paths, use os
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'my_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.db')
# This line is adding sqlite:/// with the path of your database

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
db.create_all()

login_mngr = LoginManager(app)
login_mngr.login_view = 'login'

# database connection
# db_info = {
#     'host': 'localhost',
#     'database': 'my_db',
#     'psw': 'THISmann',
#     'user': 'root',
#     'port': ''
# }

# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
