import os


class Configs:

    def __init__(self):
        self.token_endpoint = os.getenv("MPESA_TOKEN_ENDPOINT")
        self.stk_request_endpoint = os.getenv("STK_REQUEST_ENDPOINT")
        self.callBack = os.getenv("CALLBACK_ENDPOINT")
        self.logsDir = os.getenv("LOG_FILE_DIR")
        self.dbUrl = os.getenv("DB_URL")
