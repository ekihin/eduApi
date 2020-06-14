import requests
from config import *
payload = {
    'action':'delete_course',
    'id':'1519'
}
reqs = requests.delete(f'{HOST}/api/mgr/sq_mgr/',data=payload,headers=contentType1)
print(reqs.json())