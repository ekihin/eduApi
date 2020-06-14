from lib.courseLib import *
from config import *
import time

#新增一个系统中不存在的课程
courseNmae= '添加课程自动化' + str(int(time.time()*1000))
retDict = course_add(courseNmae,'添加课程自动化描述',1)
if retDict['retcode'] == 0 :
    print(">>>>>>>>>>>新增课程测试通过")
    id = retDict['id']
    retDict2 = course_list(1,500)
    flag = False
    for dict in retDict2['retlist']:
        if dict['id'] == id:
            print(">>>>>>>>>>>列出课程测试通过："+str(dict['id']))
            flag = True
            break
    if flag == False:
        print(">>>>>>>>>>>列出课程测试不通过！")
else:
    print(">>>>>>>测试不通过")