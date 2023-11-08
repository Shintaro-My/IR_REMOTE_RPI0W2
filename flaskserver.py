from flask import Flask, Blueprint, request, render_template, send_from_directory
from flask_restful import Resource, Api
import os

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


bp = Blueprint('util', __name__)
api = Api(bp)
adc = ADC_I2C_TINY202()
class CdsResource(Resource):
    def get(self):
        return { 'value': adc.get() }

api.add_resource(CdsResource, '/util/cds')

app.register_blueprint(bp, url_prefix='/api')

# クライアントサイドで使う画像ファイルなどは、client/publicフォルダに入れる
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path:
        return send_from_directory('client/dist', path)
    return render_template('index.html')

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=False, host='0.0.0.0', port=5555)