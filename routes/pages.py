from flask import Blueprint, render_template, request, redirect, url_for
from models.state import online_users


pages = Blueprint("pages", __name__)

@pages.route('/')
def home():
    return render_template("index.html")


@pages.route('/api')
def api():
    return render_template("api.html")

@pages.route('/healthz')
def healthz():
    return "OK", 200


@pages.route('/chat')
def chat():
    username = request.args.get('username', 'Guest')
    color = request.args.get('color', None)

    if username in online_users:
        return redirect(url_for('pages.login', error='nickname'))

    first_letter_username = username[0]
    return render_template('chat.html', username=username, color=color, flu=first_letter_username)



@pages.route('/login')
def login():
    error = request.args.get('error')
    return render_template('login.html', error=error)


@pages.route("/about")
def about():
    return render_template('about.html')
