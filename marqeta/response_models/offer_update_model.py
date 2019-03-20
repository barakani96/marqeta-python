from datetime import datetime, date
import json

class OfferUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
            return self.json_response['start_date']

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
            return self.json_response['end_date']

    def __repr__(self):
         return '<Marqeta.response_models.offer_update_model.OfferUpdateModel>'