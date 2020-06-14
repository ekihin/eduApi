import requests
from config import *
# 教官系统-新增课程
head = {'content-Type': 'application/x-www-form-urlencoded'}
dict = {'action': 'add_course',
        'data': """{
        "name":"测试接口12",
        "desc":"测试增加课程接口描述",
        "display_idx":"1"}"""
        }
r2 = requests.post(f'{HOST}/api/mgr/sq_mgr/', data=dict, headers=contentType1)
print(r2.json())

