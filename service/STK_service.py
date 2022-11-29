import base64
from datetime import datetime

import requests
from flask import request
from utility.app_configs import Configs


class StkService:

    def __init__(self):
        self.cfg = Configs()

    def create_stk_request(self, amount, phone, credentials):
        access_token = self.token(credentials)
        headers = {"Authorization": "Bearer %s" % access_token}
        times = datetime.now().strftime("%Y%m%d%H%M%S")
        password = "779208" + "48acf749d2718a5da64ed23c5cdebe7c776708cad7eafb0dfcf60d9fbc7aeaae" + times

        datapass = base64.b64encode(password.encode('utf-8'))
        passcode = (datapass.decode('utf-8'))

        data = {
            "BusinessShortCode": "779208",
            "Password": passcode,
            "Timestamp": times,
            "TransactionType": "CustomerBuyGoodsOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": "639058",
            "PhoneNumber": phone,
            "CallBackURL": self.cfg.callBack,
            "AccountReference": phone,
            "TransactionDesc": "Trial Txn"
        }

        res = requests.post(self.cfg.stk_request_endpoint, json=data, headers=headers)
        return res.json()

    def stk_callback_handler(self):
        data = request.get_json()
        print(data)
        return 'Ok'

    def token(self, credentials):
        querystring = {"grant_type": "client_credentials"}
        payload = ""
        headers = {"Authorization": "Basic %s" % credentials}
        response = requests.request("GET", self.cfg.token_endpoint, data=payload, headers=headers, params=querystring)
        token = response.json()
        acc_token = token['access_token']
        print("Successfully Generated Access Token :)")
        return acc_token

    def Basicauth_code(self, key, secret):
        consumer_key = key
        consumer_secret = secret
        combination = consumer_key + ":" + consumer_secret
        print("Auth key Has been created :) ")
        return base64.b64encode(combination.encode()).decode()
