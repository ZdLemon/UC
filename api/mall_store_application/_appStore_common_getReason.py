# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time


params = {
    "type": 3, # 类型: 3退货 4换货
}

def _appStore_common_getReason(params=params, access_token=access_token):
    """
    获取各种退换货原因
    /appStore/common/getReason
    """

    url = f"{BASE_URL}/appStore/common/getReason"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
