import os
import uuid

from QAWebServer.basehandles import QABaseHandler
from QUANTAXIS.QASetting.QALocalize import cache_path
from QUANTAXIS.QAUtil.QAParameter import RUNNING_STATUS
from QUANTAXIS.QAUtil.QASetting import DATABASE


class UploaderHandler(QABaseHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With")
        self.set_header("Access-Control-Allow-Methods", "HEAD, GET, POST, PUT, PATCH, DELETE")

    def post(self):
        path = 'a'
        with open(path, 'wb') as out:
            body = self.request.body
            print(body)
            out.write(bytes(body))
        self.write('WRONG')

    def put(self):
        path = 'a'
        with open(path, 'wb') as out:
            body = self.request.body
            print(body)
            out.write(bytes(body))
        self.write('WRONG')

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()