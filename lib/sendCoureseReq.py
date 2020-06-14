from  lib.courseLib import *
import json

#执行每一条测试用例，并且返回结果字典
def sendCoureseReq(row):

    # 将字符串转化为字典
    retJsonData = json.loads(row[5])    #预设的请求体

    retDict = []
    if row[4] == 'add':
        courseName = retJsonData['name']
        courseName = courseName.replace('{{courseName}}', '自动化测试' + str(int(time.time() * 1000)))
        retDict = course_add(courseName, retJsonData['desc'], retJsonData['display_idx'])
    elif row[4] == 'delete':
        retDict = course_del(retJsonData['id'])

    elif row[4] == 'list':
        retDict = course_list(retJsonData['pagenum'], retJsonData['pagesize'])

    elif row[4] == 'modify':
        pass
    else:
        pass
    return retDict