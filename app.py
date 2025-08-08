from flask import Flask
from flask_socketio import SocketIO
from routes.api import api as api_blueprint
from routes.pages import pages as pages_blueprint
from sockets.events import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(pages_blueprint)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json'
app.config['JSON_AS_ASCII'] = False


if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app, host='0.0.0.0', port=80, debug=True)

