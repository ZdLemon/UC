# coding:utf-8

from api.basic_services._auth_scenes_permission_getBaseMonthlyReportData import _auth_scenes_permission_getBaseMonthlyReportData
from api.basic_services._login import _login
from datetime import date, timedelta
import os

def getBaseMonthlyReportData():
    "获取公开补报时间"
    
    today = date.today().day  
    r = _login(username="test02").json()
    data = _auth_scenes_permission_getBaseMonthlyReportData(r["data"]["access_token"]).json()["data"]
    
    if int(data["startDay"]) <= int(today) <= int(data["endDay"]) and int(today) <= 3: # 公开补报时间
        return 3
    elif int(today) <= int(data["deadline"]) and int(today) <= 8: # 非公开补报时间，且未超过补报截止时间
        return 8
    elif int(today) < 15 and int(today) % 2 == 0: # 未超过15日月结时间，当月退
        return 15
    elif int(today) < 15 and int(today) % 2 != 0:
        return 14
    elif int(today) > 15 and (int(today) % 3 == 0): # 超过月结时间，隔月退
        return 16
    elif int(today) > 15 and int(today) % 3 != 0:
        return 17