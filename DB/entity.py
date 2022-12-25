
from sqlalchemy import Column, String,TIMESTAMP,INTEGER,DECIMAL
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class ClientData():
    __tablename__ = 'tbl_client_data'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)



class Transaction(base):
    __tablename__ = 'transactions'
    transactions_id = Column(INTEGER,primary_key=True,nullable=False)
    client_trans_id = Column(String,nullable=False)
    business_short_code = Column(String,nullable=False)
    timestamp_received= Column(String,nullable=False)
    transaction_type=Column(String,nullable=False)
    amount= Column(DECIMAL,nullable=False)
    short_code= Column(String,nullable=False)
    phone_number =Column(String,nullable=False)
    callback_url= Column(String,nullable=False)
    client_callback_url= Column(String)
    client_callback_sent= Column(String,default= 'NOT-SENT')
    request_status = Column(String,nullable=False)
    record_status= Column(String,nullable=False)
    account_reference = Column(String,nullable=False)
    transaction_desc = Column(String,nullable=False)
    merchant_request_id= Column(String)
    response_code= Column(String)
    customer_message = Column(String)
    checkout_request_id= Column(String)
    response_description= Column(String)
    result_code= Column(String)
    result_description= Column(String)
    mpesa_receipt_number = Column(String)
    timestamp_completed= Column(String)
    result_json= Column(String)
    username= Column(String,nullable=False)
    created_by= Column(String)
    created_at=Column(TIMESTAMP,nullable=False)
    customer_name= Column(String)
    customer_check = Column(String)
    date_transaction_closed= Column(TIMESTAMP)

