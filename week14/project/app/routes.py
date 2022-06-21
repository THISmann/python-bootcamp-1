from flask import Flask, request
import flask
import flask_wtf
import wtforms
from app import app, db
# from app.forms import Addtodo
# from app.models import MyModel, Todo


@app.route("/")
def index():
    return flask.render_template("index.html")
