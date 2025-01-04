from flask import Blueprint,render_template
from flask_socketio import SocketIO, emit

pages = Blueprint('pages', __name__)
soc = SocketIO()

imageDataGlobal = None

@pages.route('/')
def index():
    return render_template('index.html')
@soc.on('client_image')
def handle_client_image(imageData):
    print('Received image from client.')
    imageDataGlobal = imageData
    

@pages.route('/capture', methods=['POST'])
def capture():
    emit('server_request_image')
    while imageDataGlobal is not None:
        print('Image data received.')
        break