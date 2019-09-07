from QUANTAXIS.TSBoosting.TSBoosting import TS_Boosting_predict
from QAWebServer.basehandles import QABaseHandler
from QUANTAXIS.QAUtil import QASETTING
import pandas as pd
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas

class PredictHandler(QABaseHandler):
    def get(self,):
        start = self.get_argument('start')
        end = self.get_argument('end')
        by = 'D'
        databaseid = 'mydatabase'
        collectionid = 'rawdatatest'
        TS_Boosting_predict(start=start,end=end,by=by,databaseid=databaseid,collectionid=collectionid)
        client = QASETTING.client
        database = client.mydatabase
        coll_prediction = database['prediction']
        col = coll_prediction.find()
        outcome = pd.DataFrame(list(col))
        outcome = outcome.drop(columns='_id')
        data = QA_util_to_json_from_pandas(outcome)
        self.write({'result': data})