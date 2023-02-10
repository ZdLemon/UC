# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_sys_lclFee_list(access_token=access_token):
    """
    获取拼箱费列表
    /mgmt/sys/lclFee/list
    """

    url = f"{BASE_URL}/mgmt/sys/lclFee/list"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
