# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_sys_getProvinceList(access_token=access_token):
    """
    获取省份信息
    /mgmt/sys/getProvinceList
    """

    url = f"{BASE_URL}/mgmt/sys/getProvinceList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
