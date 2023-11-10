from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
#from flask_socketio import SocketIO, send, emit
import os
from threading import Lock

from flask_bp import cds, irdb

###### CONFIG ######
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
# EXPLAIN_TEMPLATE_LOADING = True
###### ###### ######

app = Flask(__name__,
            static_url_path='/resource', 
            static_folder='client/dist/resource',
            template_folder='client/dist')
CORS(app)
app.config.from_object(__name__)


# API
app.register_blueprint(cds.bp, url_prefix='/api') # /api/cds
app.register_blueprint(irdb.bp, url_prefix='/api') # /api/ir, /api/ir/<key>


# クライアントサイドで使う画像ファイルなどは、client/publicフォルダに入れる
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path:
        return send_from_directory('client/dist', path)
    return render_template('index.html') # , async_mode=socketio.async_mode


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=False, host='0.0.0.0', port=5555)