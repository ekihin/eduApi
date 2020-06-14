import requests
from config import *
import time

#教官系统-用户登录：
def login(username,password):
    dict = {
            'username':f'{username}',
            'password':f'{password}'
    }
    try:
        reqs = requests.post(f'{HOST}/api/mgr/loginReq',data=dict,headers=contentType1)
        return(reqs.cookies['sessionid'])
    except:
        return {"recode":999,"reaaon":"程序异常"}

print(login('auto','sdfsdfsdf'))