from flask import Blueprint
from flask_restful import Resource, Api
import time

from src.adc_i2c_tiny202 import ADC_I2C_TINY202

bp = Blueprint('util', __name__)
api = Api(bp)
adc = ADC_I2C_TINY202()
class CdsResource(Resource):
    def get(self):
        return { 'value': adc.get(), 'millis': int(time.time()) }
api.add_resource(CdsResource, '/cds')