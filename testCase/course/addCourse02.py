from lib.courseLib import *
from config import *
import time

#新增一个系统中不存在的课程
courseNmae= '添加课程自动化' + str(int(time.time()*1000))
retDict = course_add(courseNmae,'添加课程自动化描述',1)

#新增同名课程
retDict2 = course_add(courseNmae,"添加同名课程",1)
if retDict2['retcode'] == 2:
    print(">>>>>>>>>>>>>>新增同名课程用例通过")
    num = 0
    for item in course_list(1,500)['retlist']:
        if item['name'] == courseNmae:
            num = num + 1
    if num == 1:
        print(">>>>>>>>>>>>>列出课程测试通过")
    else:
        print(">>>>>>>>>>>>>列出课程测试不通过")
else:
    print(">>>>>>>>>测试不通过")