from flask import jsonify

from utility.check_validity import Validity
from models.response import Response
from service.STK_service import StkService


class API:

    def __init__(self):
        self.stk = StkService()
        self.valid = Validity()

    def mpesa_stk_api_controller(self, data):
        amount = data.get('amount')
        phone = data.get('phone')
        consumer_key = data.get('consumer_key')
        consumer_secret = data.get('consumer_secret')
        mobile = phone

        # creating base64 encode credentials

        if self.valid.check_phone(mobile):
            credentials = self.stk.Basicauth_code(consumer_key, consumer_secret)
            return self.stk.create_stk_request(amount, phone, credentials)
        else:
            return jsonify(Response("100", "FAILED", "Phone no validation error", "!").__dict__)

    def incoming(self):
        # check on response conversion
        return self.stk.stk_callback_handler()
