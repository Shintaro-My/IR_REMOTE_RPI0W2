from flask import Blueprint
from flask_restful import Resource, Api

from src.sqlite import DB
from src.ir_string import encode, decode

bp = Blueprint('source', __name__)
api = Api(bp)
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

class IRResource(Resource):
    def get(self):
        data = get_all_ir()
        print(data)
        return data
    
api.add_resource(IRResource, '/ir')