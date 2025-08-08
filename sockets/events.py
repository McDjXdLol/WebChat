from flask import request
from flask_socketio import SocketIO, emit
from models.state import online_users, sid_to_nickname, unique_users, messages
from datetime import datetime
from bot import Bot
import random

socketio = SocketIO()
bot = Bot()
unique_users_count = 0

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