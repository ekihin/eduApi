import requests
from config import *

#教官系统-修改课程
head = {'content-Type':'application/x-www-form-urlencoded'}
dict6 = {
        'action':'modify_course',
        'id':'1516',
        'newdata':"""{
                "name":"大学英语3123125566",
                "desc":"大学英语修改",
                "display_idx":"0"
        }"""
}
reqs = requests.put(f'{HOST}/api/mgr/sq_mgr/',data=dict6,headers=contentType1)
print(reqs.json())