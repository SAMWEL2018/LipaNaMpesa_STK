from flask import Flask
from controller.api_controller import API
from flask import request
from dotenv import load_dotenv
import utility.app_logs as appLog

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
    return api.mpesa_stk_api_controller(data)


@app.route('/callback', methods=['POST'])
def callback():
    return api.incoming()


if __name__ == '__main__':
    app.run(debug=True, port=9191)

