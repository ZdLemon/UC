# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber

import requests


def _mgmt_prmt_getMemberIdentity(access_token=access_token):
    """
    获取所有顾客身份类型
    /mgmt/prmt/getMemberIdentity
    """

    url = f"{BASE_URL}/mgmt/prmt/getMemberIdentity"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
