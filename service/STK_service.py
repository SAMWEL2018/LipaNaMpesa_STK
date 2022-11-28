import base64
from datetime import datetime

import requests
from flask import request


class StkService:
    my_endpoint = "https://webhook.site/ffca2f05-2b8d-4a5e-854c-0a8841840a57"
    my_endpoint1 = "https://5702-197-248-58-101.eu.ngrok.io"

    def create_stk_request(self, amount, phone, credentials):
        endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        access_token = self.token(credentials)
        headers = {"Authorization": "Bearer %s" % access_token}
        Timestamp = datetime.now()
        times = Timestamp.strftime("%Y%m%d%H%M%S")
        password = "174379" + "48acf749d2718a5da64ed23c5cdebe7c776708cad7eafb0dfcf60d9fbc7aeaae" + times
        print("password", password)
        datapass = base64.b64encode(password.encode('utf-8'))
        passcode = (datapass.decode('utf-8'))

        data = {
            "BusinessShortCode": "360402",
            "Password": passcode,
            "Timestamp": times,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": "639058",
            "PhoneNumber": phone,
            "CallBackURL": self.my_endpoint1+"/callback",
            "AccountReference": "Testpay",
            "TransactionDesc": "Testing"
        }

        res = requests.post(endpoint, json=data, headers=headers)
        return res.json()

    def stk_callback_handler(self):
        data = request.get_json()
        print(data)
        return 'Ok'

    def token(self,credentials):
        url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
        querystring = {"grant_type": "client_credentials"}
        payload = ""
        headers = {"Authorization": "Basic %s" % credentials}
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        token = response.json()
        acc_token = token['access_token']
        print("Token is : ",acc_token)
        return acc_token

    def Basicauth_code(self,key,secret):
        consumer_key = key
        consumer_secret = secret
        combination = consumer_key + ":" + consumer_secret
        print("Auth from key and secret : ",base64.b64encode(combination.encode()).decode())
        return base64.b64encode(combination.encode()).decode()
