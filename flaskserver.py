from flask import Flask, render_template, send_from_directory
import os

###### CONFIG ######
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
# EXPLAIN_TEMPLATE_LOADING = True
###### ###### ######

app = Flask(__name__,
            static_url_path='/resource', 
            static_folder='client/dist/resource',
            template_folder='client/dist')
app.config.from_object(__name__)


# クライアントサイドで使う画像ファイルなどは、client/publicフォルダに入れる
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path:
        return send_from_directory('client/dist', path)
    return render_template('index.html')

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=False, host='0.0.0.0', port=999)