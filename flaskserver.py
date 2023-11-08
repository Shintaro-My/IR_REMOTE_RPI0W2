from flask import Flask, Blueprint, request, render_template, send_from_directory
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send, emit
import os
from threading import Lock

from src.adc_i2c_tiny202 import ADC_I2C_TINY202

###### CONFIG ######
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
# EXPLAIN_TEMPLATE_LOADING = True
###### ###### ######

app = Flask(__name__,
            static_url_path='/resource', 
            static_folder='client/dist/resource',
            template_folder='client/dist')
app.config.from_object(__name__)

# API
bp = Blueprint('util', __name__)
api = Api(bp)
adc = ADC_I2C_TINY202()
class CdsResource(Resource):
    def get(self):
        return { 'value': adc.get() }
api.add_resource(CdsResource, '/util/cds')
app.register_blueprint(bp, url_prefix='/api')

# WebSocket
socketio = SocketIO(app, cors_allowed_origins='*')
thread = None
thread_lock = Lock()
def background_thread():
    while True:
        socketio.sleep(1)
        socketio.emit('cds', {'value': adc.get()})

# クライアントサイドで使う画像ファイルなどは、client/publicフォルダに入れる
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path:
        return send_from_directory('client/dist', path, async_mode=socketio.async_mode)
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
    print(app.url_map)
    socketio.run(debug=False, host='0.0.0.0', port=5555)