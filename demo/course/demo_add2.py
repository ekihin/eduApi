import requests
from config import *
import time
#教官系统-新增课程2
head = {'content-Type':'application/json','charset':'utf-8'}
now = int(time.time())
dict1 = f'''{{
        "action":"add_course_json",
        "data":{{
                "name":"增加接口{now}",
                "desc":"初中化学课程",
                "display_idx":"4"
        }}
}}'''
dict1 = dict1.encode(encoding='utf-8')
r3 =  requests.post(f'{HOST}/apijson/mgr/sq_mgr/',data=dict1,headers=head)
print(r3.json())