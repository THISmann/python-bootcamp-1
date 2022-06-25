from flask import Flask, request, jsonify
import flask
import flask_wtf
import wtforms
from app import app, db
#from flask_user import roles_required

# from app.forms import Addtodo
# from app.models import MyModel, Todo


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/register")
def register():
    return flask.render_template("register.html")


@app.route("/create-task")
def create_task():
    return flask.render_template("create-task.html")


@app.route("/all-task")
def all_task():
    return flask.render_template("all-task.html")


@app.route("/user/<user>")
def task_user(user):
    return flask.render_template("task.html", username=user)


@app.route("/task/<task_id>")
def get_task_id(task_id):
    return flask.render_template("user.html", task_id=task_id)


@app.route("/task/<task_id>/update")
def update_task(task_id):
    return flask.render_template("user.html", task_id=task_id)


@app.route("/task/<task_id>/delete")
def delete_task(task_id):
    return flask.render_template("user.html", task_id=task_id)


@app.route('/api/tasks/')
def task():
    task1 = {
        'Code': 'task-12 project12 ',
        'description': "rename the website ",
        'date': "20-10-2022"
    }
    return jsonify(task1)

# @route('/admin/dashboard')    # @route() must always be the outer-most decorator
# @roles_required('Admin')
# def admin_dashboard():
#     return flask.render_template("dashboard.html")
    # render the admin dashboard
