from flask import render_template
from app import app
from app.forms import LoginForm
from datetime import datetime 

@app.route("/ping")
def ping():
    return "Pong!"


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'mocked_user'}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!",
            "time": datetime.now()
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!" ,
            "time": datetime.now()
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
