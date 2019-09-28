from QUANTAXIS.TSBoosting.TSBoosting import TS_Boosting_predict
from QAWebServer.basehandles import QABaseHandler
from QUANTAXIS.QAUtil import QASETTING
import pandas as pd
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas
import json
import time

class TestHandler(QABaseHandler):
    def set_default_headers(self):
        print("setting headers!!! analyze")
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With, x-token")
        self.set_header("Access-Control-Allow-Methods", "HEAD, GET, POST, PUT, PATCH, DELETE")
    def get(self):
        client = QASETTING.client
        database = client.mydatabase
        collection = database.uploaddata
        ref = collection.find()
        start = ref[0]['datetime']
        end = ref[ref.count()-1]['datetime']
        by = 'D'
        databaseid = 'mydatabase'
        collectionid = 'uploaddata'
        TS_Boosting_predict(start=start, end=end, by=by, databaseid=databaseid, collectionid=collectionid)
        print("token")
        test = {'token': 'success'}
        self.write(json.dumps(test))

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()
