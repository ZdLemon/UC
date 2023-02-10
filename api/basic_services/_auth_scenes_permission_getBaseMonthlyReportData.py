# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _auth_scenes_permission_getBaseMonthlyReportData(access_token=access_token):
    """
    查询公开补报时间数据
    /auth/scenes/permission/getBaseMonthlyReportData
    """

    url = f"{BASE_URL}/auth/scenes/permission/getBaseMonthlyReportData"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
