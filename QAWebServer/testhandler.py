from QUANTAXIS.TSBoosting.TSBoosting import TS_Boosting_predict
from QAWebServer.basehandles import QABaseHandler
from QUANTAXIS.QAUtil import QASETTING
import pandas as pd
import csv
from QUANTAXIS.QAUtil.QATransform import QA_util_to_json_from_pandas
import json
import time

# edited by jingya
import urllib.parse
####

class DownloadPredictHandler(QABaseHandler):
    def set_default_headers(self):
        print("setting headers!!! analyze")
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With, x-token")
        self.set_header("Access-Control-Allow-Methods", "HEAD, GET, POST, PUT, PATCH, DELETE")
    def get(self):
        client = QASETTING.client
        database = client.mydatabase
        prediction = database.prediction
        ref_prediction = prediction.find()
        predictionDF = pd.DataFrame(list(ref_prediction)).drop(columns = '_id')
        export_csv = predictionDF.to_csv(r'prediction.csv', index=None, header=True)
        self.set_header('Content-Type', 'text/csv')
        self.set_header('Content-Disposition', 'attachment; filename=prediction.csv')
        with open('prediction.csv', encoding="utf8") as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                self.write(str(row[0])+","+str(row[1])+"\r\n")
        # self.write(open(export_csv, encoding="utf8"))

class DownloadSampleHandler(QABaseHandler):
    def set_default_headers(self):
        print("setting headers!!! analyze")
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With, x-token")
        self.set_header("Access-Control-Allow-Methods", "HEAD, GET, POST, PUT, PATCH, DELETE")
    def get(self):
        client = QASETTING.client
        # database = client.mydatabase
        # prediction = database.prediction
        # ref_prediction = prediction.find()
        # predictionDF = pd.DataFrame(list(ref_prediction)).drop(columns = '_id')
        # export_csv = predictionDF.to_csv(r'prediction.csv', index=None, header=True)
        self.set_header('Content-Type', 'text/csv')
        self.set_header('Content-Disposition', 'attachment; filename=PredicT_Sample_Data.csv')
        with open('../testData/daily-total-female-births.csv', encoding="utf8") as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                self.write(str(row[0])+","+str(row[1])+"\r\n")
        # with open('prediction.csv', encoding="utf8") as f:
        #     csv_reader = csv.reader(f, delimiter=',')
        #     for row in csv_reader:
        #         self.write(str(row[0])+","+str(row[1])+"\r\n")
        

class TestHandler(QABaseHandler):
    def set_default_headers(self):
        print("setting headers!!! analyze")
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With, x-token")
        self.set_header("Access-Control-Allow-Methods", "HEAD, GET, POST, PUT, PATCH, DELETE")
    def get(self):
        client = QASETTING.client
        
        # edited by jingya
        uri_json = urllib.parse.urlparse(self.request.uri)
        query_json = urllib.parse.parse_qs(uri_json.query)
        username = query_json['username'][0]
        # print("in test handler...")
        # print(username)
        # print(type(username))
        ####
        
        database = client.mydatabase
        
        # edited by jingya
        collection = database[username]
        ####
        
        #collection = database.uploaddata
        ref = collection.find()
        start = ref[0]['datetime']
        end = ref[ref.count()-1]['datetime']
        by = 'D'

        # edited by jingya
        collectionid = username
        ####
        
        databaseid = 'mydatabase'
        #collectionid = 'uploaddata'
        TS_Boosting_predict(start=start, end=end, by=by, databaseid=databaseid, collectionid=collectionid)

        collection_prediction = database.prediction
        ref_prediction = collection_prediction.find()
        prediction = pd.DataFrame(list(ref_prediction)).drop(columns = '_id')

        prediction_json = {
            'yAxisData': list(prediction['predict']),
            'xAxisData': list(map(lambda x : x.split(' ')[0],list(prediction['datetime']))),
            'label': 'Future',
            'colorPicked': '#519e19'
        }



        collection_past_predict = database.past_prediction
        ref_past_pred = collection_past_predict.find()
        past_pred = pd.DataFrame(list(ref_past_pred)).drop(columns = '_id')

        past_json = {
            'yAxisData': list(past_pred['y_t']),
            'xAxisData': list(map(lambda x: x.split(' ')[0], list(past_pred['datetime']))),
            'label': 'Past',
            'colorPicked': '#999997',
            'twoLines': True,
            'yAxisData2': list(past_pred['predict']),
            'label2': 'Past Prediction',
            'colorPicked2': '#999997',

        }
        messagebody = {
            'token': 'success',
            'past': past_json,
            'future': prediction_json
        }

        self.write(messagebody)
        #self.write(json.dumps(prediction_json))

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()
