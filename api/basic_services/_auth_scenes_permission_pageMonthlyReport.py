# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "onMonth": None,
    "cardNo": 16738855,
    "pageNum": 1,
    "pageSize": 10
}


def _auth_scenes_permission_pageMonthlyReport(params=params, access_token=access_token):
    """
    云商补报管理列表
    /auth/scenes/permission/pageMonthlyReport
    """

    url = f"{BASE_URL}/auth/scenes/permission/pageMonthlyReport"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.post(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
