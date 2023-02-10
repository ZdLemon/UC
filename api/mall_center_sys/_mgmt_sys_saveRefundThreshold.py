# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {"days": 1}


def _mgmt_sys_saveRefundThreshold(params=params, access_token=access_token):
    """
    设置自动退款阈值
    /mgmt/sys/saveRefundThreshold
    """

    url = f"{BASE_URL}/mgmt/sys/saveRefundThreshold"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
