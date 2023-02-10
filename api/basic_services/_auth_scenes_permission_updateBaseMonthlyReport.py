# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "startDay":"02",
    "endDay":"03",
    "startTime":"00:00",
    "endTime":"23:59",
    "deadline":"08"
}


def _auth_scenes_permission_updateBaseMonthlyReport(data=data, access_token=access_token):
    """
    获取当前用户登录缓存信息
    /auth/scenes/permission/updateBaseMonthlyReport
    """

    url = f"{BASE_URL}/auth/scenes/permission/updateBaseMonthlyReport"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r))     
        return r
