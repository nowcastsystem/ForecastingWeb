from QUANTAXIS.TSBoosting.TSBoosting import TS_Boosting_predict
from QAWebServer.basehandles import QABaseHandler
from QUANTAXIS.QAUtil import QASETTING
import pandas as pd
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas

class TestHandler(QABaseHandler):
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


