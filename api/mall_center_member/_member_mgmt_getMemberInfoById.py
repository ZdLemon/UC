# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "id": 1, # 顾客ID
}


def _member_mgmt_getMemberInfoById(params=params, access_token=access_token):
    """
    根据顾客ID获取顾客详细信息
    /member/mgmt/getMemberInfoById
    """

    url = f"{BASE_URL}/member/mgmt/getMemberInfoById"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
