from datetime import datetime, date
from marqeta.response_models.fulfillment import Fulfillment
import json

class CardUpdateRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def expedite(self):
        if 'expedite' in self.json_response:
            return self.json_response['expedite']

    @property
    def fulfillment(self):
        if 'fulfillment' in self.json_response:
            return Fulfillment(self.json_response['fulfillment'])

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

    def __repr__(self):
         return '<Marqeta.response_models.card_update_request.CardUpdateRequest>'