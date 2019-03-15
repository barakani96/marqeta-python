from datetime import datetime, date
import json

class AccountModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'code' : self.code,
           'description' : self.description,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def code(self):
        if 'code' in self.json_response:
            return self.json_response['code']

    @property
    def description(self):
        if 'description' in self.json_response:
            return self.json_response['description']

    def __repr__(self):
         return '<Marqeta.response_models.account_model.AccountModel>'