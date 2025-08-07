import os
from datetime import datetime

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_socketio import SocketIO, emit, disconnect
from bot import Bot

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback')
socketio = SocketIO(app)

connected_users = {}  # {nickname: sid}
sid_to_nickname = {}  # {sid: nickname}
messages = []  # [{"datetime": "{datetime}","message": "{msg}","username": "{nick}}"}]

bot = Bot()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/api')
def api():
    return jsonify(messages)


@app.route('/healthz')
def healthz():
    return "OK", 200


@app.route('/chat')
def chat():
    username = request.args.get('username', 'Guest')
    color = request.args.get('color', '#ffffff')

    if username in connected_users:
        return redirect(url_for('login', error='nickname'))

    first_letter_username = username[0]
    return render_template('chat.html', username=username, color=color, flu=first_letter_username)


@app.route('/login')
def login():
    error = request.args.get('error')
    return render_template('login.html', error=error)


@socketio.on('connect')
def handle_connect():
    print("New connection:", request.sid)


@socketio.on('register_user')
def handle_register_user(data):
    username = data.get("username")
    if username in connected_users:
        emit('nickname_taken')
        disconnect()
        return

    connected_users[username] = request.sid
    sid_to_nickname[request.sid] = username
    print(f"Registered: {username} ({request.sid})")
    emit('registration_successful')


@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    nickname = sid_to_nickname.pop(sid, None)
    if nickname:
        connected_users.pop(nickname, None)
        print(f"{nickname} disconnected - ({sid})")
    else:
        print(f"Unknown client disconected - ({sid})")


@socketio.on('send_message')
def handle_message(data):
    print('Received:', data)


    emit('receive_message', data, broadcast=True)

    messages.append({"message": data["text"], "username": data['username'],
                     "datetime": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
    if bot.is_command(data["text"]):
        response = bot.get_reply(data["text"])
        if response:
            emit('receive_message', {
                'username': 'Bot',
                'color': '#00ffff',
                'text': response
            }, broadcast=True)

        messages.append({"message": response, "username": "Bot",
                         "datetime": datetime.now().strftime("%d.%m.%Y %H:%M:%S")})


if __name__ == '__main__':
    socketio.run(app, debug=True)
