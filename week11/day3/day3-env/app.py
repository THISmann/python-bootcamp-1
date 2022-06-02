from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=5500)


@app.route('/<username>')
def homepage(username):
    return render_template('homepage.html', name=username)


@app.route('/articles')
def articles():
    return render_template('articles.html', datas=['one', 'two'])
