from datetime import datetime, date
from marqeta.response_models.offer_order_balances import OfferOrderBalances
from marqeta.response_models.offer_order_aggregated_balances import OfferOrderAggregatedBalances
from marqeta.response_models.funding import Funding
from marqeta.response_models.offer_model import OfferModel
import json

class OfferOrderResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'token' : self.token,
           'order_balances' : self.order_balances,
           'order_aggregated_balances' : self.order_aggregated_balances,
           'funding' : self.funding,
           'offer' : self.offer,
           'last_transaction_date' : self.last_transaction_date,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def order_balances(self):
        if 'order_balances' in self.json_response:
            return OfferOrderBalances(self.json_response['order_balances'])

    @property
    def order_aggregated_balances(self):
        if 'order_aggregated_balances' in self.json_response:
            return OfferOrderAggregatedBalances(self.json_response['order_aggregated_balances'])

    @property
    def funding(self):
        if 'funding' in self.json_response:
            return Funding(self.json_response['funding'])

    @property
    def offer(self):
        if 'offer' in self.json_response:
            return OfferModel(self.json_response['offer'])

    @property
    def last_transaction_date(self):
        if 'last_transaction_date' in self.json_response:
                return datetime.strptime(self.json_response['last_transaction_date'], '%Y-%m-%d').date()

    def __repr__(self):
         return '<Marqeta.response_models.offer_order_response.OfferOrderResponse>'