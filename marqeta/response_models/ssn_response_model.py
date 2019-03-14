from datetime import datetime, date
import json

class SsnResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'ssn' : self.ssn,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def ssn(self):
        if 'ssn' in self.json_response:
            return self.json_response['ssn']

    def __repr__(self):
         return '<Marqeta.response_models.ssn_response_model.SsnResponseModel>'