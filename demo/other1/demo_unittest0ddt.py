import unittest
from lib.excelManager import readExcel
from ddt import ddt,data
from lib.sendCoureseReq import sendCoureseReq
import json


filePath = r'G:/pycharm_workspace/eduApi/data/教管系统-测试用例V1.2 .xls'
retDataList = readExcel(filePath,0)
# mydata = [[1,2,3],[3,4,7],[1,3,5]]


@ddt
class DdtDemo(unittest.TestCase):

    @data(*retDataList)
    def test09(self,row):
        retDict = sendCoureseReq(row)
        colus6 = json.loads(row[6])
        v_reason = ''
        if 'reason' in retDict.keys():
            v_reason = retDict['reason']
        self.assertEqual(colus6['code'],retDict['retcode'],v_reason)
        print('>>>>>>>>测试通过')