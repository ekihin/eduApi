import requests
from config import *
# 教管系统-列出课程
dict = {
    'action':'list_course',
    'pagenum':1,
    'pagesize':20
}
r1 = requests.get(f'{HOST}/api/mgr/sq_mgr/',params=dict)
print(r1.json())