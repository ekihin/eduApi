import xlrd
import xlutils
from lib.excelManager import readExcel


filePath = r'G:/pycharm_workspace/eduApi/data/教管系统-测试用例V1.2 .xls'
savePath = r'G:/pycharm_workspace/eduApi/report/测试结果.xls'
retDictData = readExcel(filePath,2)

for i in range(0,len(retDictData)):
    pass