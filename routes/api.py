# routes/api.py
from flask import Blueprint, jsonify
from models.state import messages, unique_users, online_users
from bot import Bot

api = Blueprint('api', __name__)
bot = Bot()

@api.route('/messages_history')
def messages_history():
    return jsonify(messages)

@api.route('/unique_users')
def unique_users_count_api():
    return jsonify({
        "unique_users": sorted(list(unique_users)),
        "amount": len(unique_users)
    })

@api.route('/users_online')
def users_online():
    return jsonify({
        "online_users": list(online_users.keys()),
        "amount": len(online_users)
    })

@api.route('/bot_commands')
def bot_commands():
    return jsonify({
        "commands": [
            {"name": f"!{k}", "description": v[1]}
            for k, v in bot.commands.items()
        ],
        "amount": len(bot.commands)
    })

@api.route('/stats')
def stats():
    return jsonify({
        "unique_users": len(unique_users),
        "online_users": len(online_users),
        "total_messages": len(messages)
    })

@api.route('/about')
def about_api():
    return jsonify({
        "name": "Chat Web",
        "version": "1.0.0-iguess",
        "description": "A simple chat application with a bot.",
        "author": "McDjXdLol",
        "license": "MIT"
    })
