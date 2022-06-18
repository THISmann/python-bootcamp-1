import flask
import os
import flask_sqlalchemy
import flask_migrate

from app import app

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

class MyModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(64), index=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(64), index=True)
    
    def save_task_to_db(self, id , detail):
        model = self(id=id, details=detail)
        db.session.add(model1)
        db.session.commit()
        

