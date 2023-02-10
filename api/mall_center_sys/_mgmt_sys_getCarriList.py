# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_sys_getCarriList(access_token=access_token):
    """
    查询所有的运费模板
    /mgmt/sys/getCarriList
    """

    url = f"{BASE_URL}/mgmt/sys/getCarriList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
