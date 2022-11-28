from flask import Flask
from controller.api_controller import API
from flask import request, jsonify, json
from flask import jsonify

app = Flask(__name__)
api = API()

@app.route("/", methods=['GET'])
def index():
    # Initila Api Call Test Also test If up is running
    return '{"api_status" : "MPESA Service is Up and running" }'


@app.route("/pay", methods=['GET'])
def pay():
    return api.mpesa_stk_api_controller(request.get_json())


@app.route('/callback', methods=['POST'])
def callback():
    return api.incoming()


if __name__ == '__main__':
    app.run(debug=True, port=9191)

