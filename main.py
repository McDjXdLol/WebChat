import os
from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_socketio import SocketIO, emit
from bot import Bot
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback')
socketio = SocketIO(app)

online_users = {}  # {username: color}
sid_to_nickname = {}  # {sid: username}
unique_users = set() # Set to store unique usernames
unique_users_count = 0 # Counter for unique users
messages = []  # List to store chat messages

bot = Bot()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/api')
def api():
    return render_template("api.html")


@app.route('/api/messages_history')
def messages_history():
    return jsonify(messages)


@app.route('/api/unique_users')
def unique_users_count_api():
    if not unique_users:
        return jsonify({"unique_users": [], "amount": 0})
    uniq_users_list = sorted(list(unique_users))
    return jsonify({"unique_users": uniq_users_list, "amount": unique_users_count})


@app.route('/api/users_online')
def users_online():
    return jsonify({"online_users": list(online_users.keys()), "amount": len(online_users)})


@app.route('/healthz')
def healthz():
    return "OK", 200


@app.route('/chat')
def chat():
    username = request.args.get('username', 'Guest')
    color = request.args.get('color', None)  # moze być None - wtedy nadamy samemu

    if username in online_users:
        return redirect(url_for('login', error='nickname'))

    first_letter_username = username[0]
    return render_template('chat.html', username=username, color=color, flu=first_letter_username)


@app.route('/login')
def login():
    error = request.args.get('error')
    return render_template('login.html', error=error)


@app.route("/about")
def about():
    return render_template('about.html')


@socketio.on('user_typing')
def handle_typing(data):
    emit('show_typing', data, broadcast=True, include_self=False)


@socketio.on('user_count')
def handle_user_count():
    username = sid_to_nickname.get(request.sid)
    emit('update_users_online', {'users': [{'username': u, 'color': c} for u, c in online_users.items()], "user_color": online_users.get(username)}, broadcast=True)


@socketio.on('connect')
def handle_connect():
    print("New connection:", request.sid)


@socketio.on('register_user')
def handle_register(data):
    global unique_users_count
    username = data.get('username')
    color = data.get('color')

    sid = request.sid
    if username in online_users:
        emit('nickname_taken')
        return
    if username not in unique_users:
        unique_users.add(username)
        unique_users_count += 1
        print(f"New Unique user: {username}! Total unique users: {unique_users_count}")

    if not color:
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))

    online_users[username] = color
    sid_to_nickname[sid] = username

    emit('registration_successful')

    emit('update_users_online', {'users': [{'username': u, 'color': c} for u, c in online_users.items()]}, broadcast=True)


@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    username = sid_to_nickname.get(sid)
    if username:
        online_users.pop(username, None)
        sid_to_nickname.pop(sid, None)
        emit('update_users_online', {'users': [{'username': u, 'color': c} for u, c in online_users.items()]}, broadcast=True)


@socketio.on('send_message')
def handle_message(data):
    print('Received:', data)

    emit('receive_message', data, broadcast=True)

    messages.append({
        "message": data["text"],
        "username": data['username'],
        "datetime": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    })

    if bot.is_command(data["text"]) or data["text"].startswith('/'):
        response = bot.get_reply(data["text"])
        if response:
            emit('receive_message', {
                'username': 'Bot',
                'color': '#00ffff',
                'text': response
            }, broadcast=True)

            messages.append({
                "message": response,
                "username": "Bot",
                "datetime": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            })


if __name__ == '__main__':
    socketio.run(app, debug=True)
