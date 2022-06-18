from flask import Flask

from app import app, db

from app.models import MyModel , Todo

@app.route("/")
def hello_world():
    return "Hello, World youande!"



# todos = MyModel.query.all()
# db.session.add(Todo(id=1 , details="TP 22"))
# db.session.commit()
print(Todo.query.all())
