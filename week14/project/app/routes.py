from flask import Flask, request, jsonify
from app.login import Login
from app.register import Register
from app.create_task import CreateTask
from app.models import Task
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


@app.route("/login", methods=("GET", "POST"))
def login():
    login = Login()
    if login.validate_on_submit():
        username = login.username.data
        password = login.password.data

        print(username, password)

    return flask.render_template("login.html", login=login)


@app.route("/register", methods=("GET", "POST"))
def register():
    register = Register()
    if register.validate_on_submit():
        username = register.username.data
        email = register.email.data
        password = register.password.data

        print(username, email, password)

    return flask.render_template("register.html", register=register)


@app.route("/create-task", methods=("GET", "POST"))
def create_task():
    create_task = CreateTask()
    if create_task.validate_on_submit():
        name = create_task.name.data
        executant = create_task.executant.data
        date_start = create_task.date_start.data
        date_end = create_task.date_end.data
        author = create_task.author.data
        description = create_task.description.data
        status = create_task.status.data

        data = Task(name=name, executant=executant, date_start=date_start,
                    date_end=date_end, author=author, description=description, status=status)
        db.session.add(data)
        db.session.commit()

    return flask.render_template("create-task.html", new_task=create_task)


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
