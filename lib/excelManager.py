import xlrd
from xlutils.copy import copy

#读取excel中的数据
#功能 ：传递excel的路径和名称，第几个工作表

def readExcel(filePath,sheet_index):
    #1-1 打开Excel.获取工作簿
    workBook = xlrd.open_workbook(filePath)
    #print(workBook.sheet_names())

    #1-2从工作簿中，获取【workSheet】对象
    workSheet = workBook.sheet_by_index(sheet_index)

    #1-3对【workSheet】工作表进行循环-逐行取出数据放入列表中
    retDataList = []
    rows = workSheet.nrows
    for i in range(1,rows):
        onerow =  workSheet.row_values(i)
        retDataList.append(onerow)

    #1-4返回数据列表
    return retDataList

#获取一份excel副本
def getNewExcel(filePath):
    #1-1 打开Excel,获取【workBook】对象
    workBook = xlrd.open_workbook(filePath,formatting_info=True)
    workBookNew = copy(workBook)
    return workBookNew

if __name__ == '__main__':
    a = readExcel(r'G:/pycharm_workspace/eduApi/data/教管系统-测试用例V1.2 .xls', 0)
    print(a)