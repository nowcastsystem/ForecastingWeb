import os
import uuid
import io
import pandas as pd
import json

from QAWebServer.basehandles import QABaseHandler
from QUANTAXIS.QASetting.QALocalize import cache_path
from QUANTAXIS.QAUtil.QAParameter import RUNNING_STATUS
from QUANTAXIS.QAUtil.QASetting import DATABASE

from QUANTAXIS.QAUtil import QASETTING
from QUANTAXIS.TSData.TSRawdata import TSRawdata
# from QUANTAXIS.TSData.TSRawdata2 import TSRawdata2
from QUANTAXIS.TSUtil.TSDate import TS_util_date2str

class UploaderHandler(QABaseHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With,  x-csrf-token")
        self.set_header("Access-Control-Allow-Methods", "HEAD, GET, POST, PUT, PATCH, DELETE")

    def post(self):
        body = self.request.body
        df = pd.read_csv(io.StringIO(body.decode('utf-8')))
        rawdata = TSRawdata(df)
        outcome = rawdata.data
        outcome = TS_util_date2str(outcome)
        outcome = json.loads(outcome.to_json(orient='records'))
        # print(df)
        myclient = QASETTING.client
        database = myclient.mydatabase
        col = database.uploaddata
        col.drop()
        col.insert_many(outcome)
        # out.write(bytes(body))
        # print(pd.read_csv(bytes(body)))
        # decoded = base64.b64decode(body)
        # df = pd.read_csv(
        #     io.StringIO(decoded.decode('utf-8')))
        # print(df)

        self.write('123')


    def put(self):
        body = self.request.body
        df = pd.read_csv(io.StringIO(body.decode('utf-8')))
        rawdata = TSRawdata2(df)
        outcome = rawdata.data
        outcome = TS_util_date2str(outcome)
        outcome = json.loads(outcome.to_json(orient='records'))
        # print(df)
        myclient = QASETTING.client
        database = myclient.mydatabase
        col = database.uploaddata
        col.drop()
        col.insert_many(outcome)
        # out.write(bytes(body))
        # print(pd.read_csv(bytes(body)))
        # decoded = base64.b64decode(body)
        # df = pd.read_csv(
        #     io.StringIO(decoded.decode('utf-8')))
        # print(df)


        self.write('123')

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()