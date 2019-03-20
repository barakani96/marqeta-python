from datetime import datetime, date
from marqeta.response_models.msa_balances import MsaBalances
from marqeta.response_models.funding import Funding
from marqeta.response_models.msa_aggregated_balances import MsaAggregatedBalances
import json

class MsaOrderResponse(object):

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
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def order_balances(self):
        if 'order_balances' in self.json_response:
            return MsaBalances(self.json_response['order_balances'])

    @property
    def purchase_amount(self):
        if 'purchase_amount' in self.json_response:
            return self.json_response['purchase_amount']

    @property
    def last_transaction_date(self):
        if 'last_transaction_date' in self.json_response:
                return datetime.strptime(self.json_response['last_transaction_date'], '%Y-%m-%d').date()

    @property
    def start_date(self):
        if 'start_date' in self.json_response:
                return datetime.strptime(self.json_response['start_date'], '%Y-%m-%d').date()

    @property
    def end_date(self):
        if 'end_date' in self.json_response:
                return datetime.strptime(self.json_response['end_date'], '%Y-%m-%d').date()

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def reward_amount(self):
        if 'reward_amount' in self.json_response:
            return self.json_response['reward_amount']

    @property
    def reward_trigger_amount(self):
        if 'reward_trigger_amount' in self.json_response:
            return self.json_response['reward_trigger_amount']

    @property
    def unloaded_amount(self):
        if 'unloaded_amount' in self.json_response:
            return self.json_response['unloaded_amount']

    @property
    def campaign_token(self):
        if 'campaign_token' in self.json_response:
            return self.json_response['campaign_token']

    @property
    def funding(self):
        if 'funding' in self.json_response:
            return Funding(self.json_response['funding'])

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def aggregated_balances(self):
        if 'aggregated_balances' in self.json_response:
            return MsaAggregatedBalances(self.json_response['aggregated_balances'])

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    def __repr__(self):
         return '<Marqeta.response_models.msa_order_response.MsaOrderResponse>'