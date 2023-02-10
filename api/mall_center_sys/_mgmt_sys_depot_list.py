# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


def _mgmt_sys_depot_list(access_token=access_token):
    """
    获取仓库信息集合
    /mgmt/sys/depot/list
    """

    url = f"{BASE_URL}/mgmt/sys/depot/list"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
    
