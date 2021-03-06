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


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(64), index=True)
    completed = db.Column(db.Boolean, index=True,
                          default=False, server_default="false")

    def __repr__(self):
        return '<Todo %r>' % self.id

    def save_task_to_db(data):
        db.session.add(data)
        db.session.commit()

    def get_tasks():
        return Todo.query.all()

    def update_task(todo_id, detail):
        task = Todo.query.get(todo_id)
        task.details = detail
        db.session.commit()

    def set_task_as_complete(todo_id):
        todo = Todo.query.get(todo_id)
        todo.completed = True
        db.session.commit()

    def delete_task(todo_id):
        task = Todo.query.get(todo_id)
        db.session.delete(task)
        db.session.commit()

    # def set_task_as_complete(self):
    #     pass

    # def __init__(self, email, password):
    #     self.email = email
    #     self.set_password(password)

    # def __repr__(self):
    #     return '<User %r>' % self.email

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return str(self.email)

    db.create_all()
