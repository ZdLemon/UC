# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {}


def _mgmt_sys_queryRefundList(access_token=access_token):
    """
    查询退款阈值修改记录
    /mgmt/sys/queryRefundList
    """

    url = f"{BASE_URL}/mgmt/sys/queryRefundList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
