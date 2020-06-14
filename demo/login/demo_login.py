import requests
from config import *
#教官系统-用户登录：
head = {'content-Type':'application/x-www-form-urlencoded','charset':'UTF-8'}
dict3 = {
        'username':'auto',
        'password':'sdfsdfsdf'
}
reqs = requests.post(f'{HOST}/api/mgr/loginReq',data=dict3,headers=head)
print(reqs.json())