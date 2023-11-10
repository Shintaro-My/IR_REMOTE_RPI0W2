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
    Value TEXT
)
"""
])
db.terminate()

def get_all_ir():
    db = DB()
    results, = db.run(["SELECT * FROM IRTable"])
    db.terminate()
    data = {}
    for res in results:
        data[res[0]] = decode(res[1])
    return data

def set_ir(name: str, value: str):
    db = DB()
    db.run([
    f"""
    INSERT INTO IRTable (Key, Value)
    VALUES (\"{name}\", \"{value}\")
    ON CONFLICT(Key)
    DO UPDATE SET Value=\"{value}\"
    """
    ])
    db.terminate()
    
class IRResource(Resource):
    def get(self):
        data = get_all_ir()
        print(data)
        return data
    def post(self):
        body = request.json
        if body is None or 'name' not in body:
            return {'type': 'error'}
        
        key = body['name']
        result = irrp.Record(GPIO=18, post=130)
        irrp.stop()
        print(result)
        set_ir( key, encode(result) )
        
        return {'type': 'success', 'data': result}
    
api.add_resource(IRResource, '/ir')