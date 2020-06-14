from lib.excelManager import *
from lib.sendCoureseReq import *
import json

filePath = r'G:/pycharm_workspace/eduApi/data/教管系统-测试用例V1.2 .xls'
savePath = r'G:/pycharm_workspace/eduApi/report/测试结果.xls'

retDataList =  readExcel(filePath,0)
workBookNew = getNewExcel(filePath)
workSheetNew = workBookNew.get_sheet(0)

for i in range(0,len(retDataList)):
    retDict = sendCoureseReq(retDataList[i])  #返回结果
    retJsonCode = json.loads(retDataList[i][6])#断言结果

    if retJsonCode['code'] == retDict['retcode']:
        print(retDataList[i][1] + '---' + retDataList[i][2] + '---' + retDataList[i][3] + ' >>>>>>>>>>>>测试通过')
        workSheetNew.write(i+1,7,'pass')
    else:
        print(retDataList[i][1] + ':' + retDataList[i][2] + ',' + retDataList[i][3] + ' >>>>>>>>>>>>测试不通过')
        workSheetNew.write(i + 1, 7, 'fail')
        if 'reason' in retDict.keys():
            workSheetNew.write(i + 1, 8, retDict['reason'])


workBookNew.save(savePath)