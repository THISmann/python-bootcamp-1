from flask import Flask

from app import app, db

from app.models import MyModel , Todo

@app.route("/")
def index():
    Todo.save_task_to_db()
    return flask.render_template('index.html')



# todos = MyModel.query.all()
# db.session.add(Todo(id=1 , details="TP 22"))
# db.session.commit()
print(Todo.query.all())
