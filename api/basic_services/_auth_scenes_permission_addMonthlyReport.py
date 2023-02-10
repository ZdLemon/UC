# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "cardNo":"16738855",
    "startTime":1659862950000,
    "endTime":1659888000000,
    "remark":"",
    "selectAll": False
}


def _auth_scenes_permission_addMonthlyReport(data=data, access_token=access_token):
    """
    新增补报
    /auth/scenes/permission/addMonthlyReport
    """

    url = f"{BASE_URL}/auth/scenes/permission/addMonthlyReport"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r))     
        return r
