# First, we are in a different file, so we need to import the app
import flask
from app.forms import User
from app import app    # app.app is package_name.variable_name


@app.route("/")
def index():
    posts = [
        {"author": "John", "body": "I love python"},
        {"author": "Fish", "body": "I love water"},
        {"author": "Herpetolog", "body": "I love pythons"},
    ]
    return flask.render_template('index.html', posts=posts)


@app.route("/help")
def func():
    return flask.render_template('help.html')


# @app.route('/myform', methods=("GET", "POST"))
# def myform():
#     form = Form()
#     if form.validate_on_submit():  # Check if the form has been filled

#         username = form.username.data  # Get
#         password = form.password.data  # The
#         bio = form.bio.data  # Data

#         print("Here is what I got from the form:")
#         print("username:", username)
#         print("password:", password)
#         print("bio:", bio)
#         # Do something with the data

#         return flask.redirect('/')
#     return flask.render_template('formulaire.html', form=form)

# # ...


@app.route('/users', methods=("GET", "POST"))
def user():
    users = User()
    if users.validate_on_submit():  # Check if the form has been filled
        firstName = users.firstName.data
        lastName = users.lastName.data
        Message = users.Message.data

        print("Here is what I got from the form:")
        print("username:", firstName)
        print("password:", lastName)
        print("bio:", Message)

    return flask.render_template('users.html', form=users)
