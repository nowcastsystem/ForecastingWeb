import os
import uuid

from QAWebServer.basehandles import QABaseHandler
from QUANTAXIS.QASetting.QALocalize import cache_path
from QUANTAXIS.QAUtil.QAParameter import RUNNING_STATUS
from QUANTAXIS.QAUtil.QASetting import DATABASE

class UploaderHandler(QABaseHandler):
    def post(self):
        # f= open("guru999.txt", "w+")
        # for i in range(10):
        #     f.write("This is line %d\r\n" % (i + 1))
        # f.close()
        #file = self.request.files['file'][0]
        #file.save('kos.csv')
        self.write('WRONG')