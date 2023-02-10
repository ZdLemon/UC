# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "storeCode":"902804",
    "cardNo":"45722864"
}


def _auth_store_restPsw(data=data, access_token=access_token):
    """
    重置服务中心密码
    /auth/store/restPsw
    """

    url = f"{BASE_URL}/auth/store/restPsw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r))     
        return r
