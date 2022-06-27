import flask
import os
import flask_sqlalchemy
import flask_migrate
from datetime import datetime
import flask_login
from app import app, db,   models
from flask_login import login_manager

# db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(64), index=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    #name = db.relationship('User', backref='task', lazy="dynamic")
    executant = db.Column(db.String(64), index=True)
    date_end = db.Column(db.DateTime, index=True, default=datetime.now)
    date_start = db.Column(db.DateTime, index=True, default=datetime.now)
    author = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64), index=True)  # relationship


class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True)
    password = db.Column(db.String(64), index=True)
    status_session = db.Column(db.String(64), index=True)
    role = db.Column(db.String(64), index=True)
    task = db.Column(db.String(64), db.ForeignKey('task.id'))
    #author = db.Column(db.String(64), db.ForeignKey('task.id'))

    def get_id(self):
        return self.id

    @login_manager.user_loader
    def load_user(id):
        return User.get(id)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
