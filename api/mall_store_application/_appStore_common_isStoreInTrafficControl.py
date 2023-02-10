# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests


def _appStore_common_isStoreInTrafficControl(access_token=access_token):
    """
    店铺是否处于交通管控
    /appStore/common/isStoreInTrafficControl
    """

    url = f"{BASE_URL}/appStore/common/isStoreInTrafficControl"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
