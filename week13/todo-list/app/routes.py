from flask import Flask
import flask , flask_wtf , wtforms
from app import app, db
from app.forms import Addtodo 

from app.models import MyModel , Todo

@app.route("/", methods=("GET", "POST"))
def index():
    users = Addtodo()
    if users.validate_on_submit():
        details = users.details.data
        Todo.save_task_to_db(Todo)
        return flask.render_template('index.html', form = users)
    else:
        Todo.get_tasks()
        return flask.render_template('index.html')
        
@app.route("complete/<int:todo_id>")
def set_task_as_complete(): 
    todo = Todo.query(todo_id)
    todo.completed = True
    db.session.commit()

# todos = MyModel.query.all()
# db.session.add(Todo(id=1 , details="TP 22"))
# db.session.commit()

#print(Todo.query.all())
