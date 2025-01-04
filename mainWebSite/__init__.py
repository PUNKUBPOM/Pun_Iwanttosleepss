from flask import Flask
from flask_socketio import SocketIO

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'PramoatV2' 
    from .pages import pages
    app.register_blueprint(pages, url_prefix='/')
    return app