from flask import Flask

from app import app, db

from app.models import MyModel

@app.route("/")
def hello_world():
    return "Hello, World youande!"



todos = MyModel.query.all()
print(MyModel.query.get(1).details)