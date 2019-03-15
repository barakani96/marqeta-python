from datetime import datetime, date
import json

class JitFundingProgramgatewayFundingSource(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'enabled' : self.enabled,
           'funding_source_token' : self.funding_source_token,
           'refunds_destination' : self.refunds_destination,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def enabled(self):
        if 'enabled' in self.json_response:
            return self.json_response['enabled']

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.json_response:
            return self.json_response['funding_source_token']

    @property
    def refunds_destination(self):
        if 'refunds_destination' in self.json_response:
            return self.json_response['refunds_destination']

    def __repr__(self):
         return '<Marqeta.response_models.jit_funding_programgateway_funding_source.JitFundingProgramgatewayFundingSource>'