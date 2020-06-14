import requests
from config import *
import time

def course_add(name,desc,display_index):
    dict = {'action': 'add_course',
            'data': f"""{{
            "name":"{name}",
            "desc":"{desc}",
            "display_idx":"{display_index}"}}"""
            }
    r2 = requests.post(f'{HOST}/api/mgr/sq_mgr/', data=dict, headers=contentType1)
    try:
        return (r2.json())
    except:
        return {"recode":999,"reaaon":"程序异常"}

def course_del(id):
    payload = {
        'action': 'delete_course',
        'id': id
    }
    try:
        r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', data=payload, headers=contentType1)
        return r.json()
    except:
        return {"recode": 999, "reaaon": "程序异常"}

def course_list(pagenum,pagesize):
    dict = {
        'action': 'list_course',
        'pagenum': pagenum,
        'pagesize': pagesize
    }
    try:
        r1 = requests.get(f'{HOST}/api/mgr/sq_mgr/', params=dict)
        return (r1.json())
    except:
        return {"recode": 999, "reaaon": "程序异常"}


def course_modify(id,name,desc,dispaly_index):
    dict6 = {
        'action': 'modify_course',
        'id': id,
        'newdata': f"""{{
                    "name":"{name}",
                    "desc":"{desc}",
                    "display_idx":"{dispaly_index}"
            }}"""
    }
    reqs = requests.put(f'{HOST}/api/mgr/sq_mgr/', data=dict6, headers=contentType1)
    try:
        return(reqs.json())
    except:
        return {"recode": 999, "reaaon": "程序异常"}

def course_add2(name,desc,display_index):
    now = int(time.time())
    dict1 = f'''{{
        "action": "add_course_json",
        "data": {{
            "name": "{name}{now}",
            "desc": "{desc}",
            "display_idx": "{display_index}"
        }}
    }}
    '''
    dict1 = dict1.encode(encoding='utf-8')
    r3 = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', data=dict1, headers=contentType2)
    try:
        return(r3.json())
    except:
        return {"recode": 999, "reaaon": "程序异常"}
