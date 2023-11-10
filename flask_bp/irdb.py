from flask import Blueprint, request
from flask_restful import Resource, Api

from src.sqlite import DB
from src.ir_string import encode, decode
from src.irrp import IRRP

bp = Blueprint('source', __name__)
api = Api(bp)
irrp = IRRP(no_confirm=True)
db = DB()
db.run([
"""
CREATE TABLE IF NOT EXISTS IRTable(
    Key   TEXT PRIMARY KEY,
    Value TEXT,
    Desc  Text
)
"""
])
db.terminate()

def get_all_ir():
    db = DB()
    results, = db.run(["SELECT * FROM IRTable"])
    db.terminate()
    data = {}
    for res in sorted(results, key=lambda r: r[0]):
        data[res[0]] = {'value': decode(res[1]), 'desc': res[2]}
    return data

def set_ir(name: str, value: str, desc: str):
    db = DB()
    db.run([
    f"""
    INSERT INTO IRTable (Key, Value, Desc)
    VALUES (\"{name}\", \"{value}\", \"{desc}\")
    ON CONFLICT(Key)
    DO UPDATE SET Value=\"{value}\", Desc=\"{desc}\"
    """
    ])
    db.terminate()

def remove_ir(name: str):
    db = DB()
    db.run([
    f"""
    DELETE FROM IRTable
    WHERE Key=\"{name}\"
    """
    ])
    db.terminate()
    
class IRResource(Resource):
    def get(self):
        return get_all_ir()
    
    def post(self):
        body = request.json
        if body is None or 'name' not in body:
            return {'type': 'error'}
        key = body['name']
        desc = body['desc'] if 'desc' in body else ''
        result = irrp.Record(GPIO=18, post=130)
        irrp.stop()
        set_ir( key, encode(result), desc )
        return {'type': 'success', 'data': result}
    
class IRItemResource(Resource):
    def get(self, key):
        data = get_all_ir()
        if key in data:
            irrp.Playback(GPIO=17, data=data[key]['value'])
            irrp.stop()
            return {'type': 'success', 'data': data[key]}
        return {'type': 'error'}
    def delete(self, key):
        data = get_all_ir()
        if key in data:
            remove_ir(key)
            return {'type': 'success'}
        return {'type': 'error'}
    
api.add_resource(IRResource, '/ir')
api.add_resource(IRItemResource, '/ir/<string:key>')