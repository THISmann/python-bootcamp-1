import flask
import os
import flask_sqlalchemy
import flask_migrate

from app import app, db

# db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(64), index=True)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.relationship('User', backhref = 'task' , lazy= "dynamic")
    executant = db.Column(db.String(64), index=True)
    date_end = db.Column(db.String(64), index=True)
    data_start = db.Column(db.String(64), index=True)
    author = db.Column(db.String(64), index=True)
    description = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64), index=True)
    author = db.Column(db.String(64), index=True) #relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True)
    password = db.Column(db.String(64), index=True)
    status_session = db.Column(db.String(64), index=True)
    role = db.Column(db.String(64), index=True)
    task = db.Column(db.String(64), db.ForeygnKey('task.id')
    author = db.Column(db.String(64), db.ForeygnKey('task.id')
    

    
class Rode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)