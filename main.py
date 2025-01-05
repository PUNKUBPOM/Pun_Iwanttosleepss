from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pramoatv2'
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('requestImage')
def handle_request_image():
    print('Received request for image')
    emit('serverRequestImage')

@socketio.on('serverGetImage')
def handle_client_image(image_data):
    try:
        if image_data.startswith("data:image/"): 
            _, encoded_data = image_data.split(",", 1)
            image_bytes = base64.b64decode(encoded_data) 
        else:
            image_bytes = image_data 

        emit('server_image', image_bytes) 

    except Exception as e:
        print(f"Error processing image: {e}")
        emit('server_error', {'error': str(e)})

@app.route('/image')
def get_image():
    return send_from_directory('static', 'received_image.jpg') 


if __name__ == '__main__':
    socketio.run(app, debug=True)
