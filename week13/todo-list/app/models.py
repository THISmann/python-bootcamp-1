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
    completed = db.Column(db.Boolean, index=True, default=False , nullable=False)
    
    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def get_tasks(self):
        return self.query.all()

    def set_task_as_complete(self):
        pass
    
    db.create_all()