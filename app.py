import json

from flask import Flask
from controller.api_controller import API
from flask import request
from dotenv import load_dotenv
import Utility.app_logs as appLog

load_dotenv(override=False, dotenv_path='.env')  # Configuration For the whole application use

app = Flask(__name__)
api = API()


@app.route("/", methods=['GET'])
def index():
    # Initila Api Call Test Also test If up is running
    return '{"api_status" : "MPESA Service is Up and running" }'


@app.route("/pay", methods=['POST'])
def pay():
    data = request.get_json()
    appLog.log(1, "Pay Request : " + str(data))
    res = api.mpesa_stk_api_controller(data)
    appLog.log(1, "Pay Response : " + str(res))
    return res


@app.route('/callback', methods=['POST'])
def callback():
    data = request.get_json()
    appLog.log(1, "Callback Request : " + str(data))
    return api.incoming()


if __name__ == '__main__':
    app.run(debug=True, port=9191)

