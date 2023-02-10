# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "dictType": "openBankCode", 
}


def _crm_lov_getCrmLovListByType(params=params, access_token=access_token):
    """
    根据业务类型获取字典列表
    /crm/lov/getCrmLovListByType
    """

    url = f"{BASE_URL}/crm/lov/getCrmLovListByType"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
