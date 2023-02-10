# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "provinceCode": None, # 省份编码
}


def _mgmt_sys_getCityList(params=params, access_token=access_token):
    """
    根据省份编码获取下属城市
    /mgmt/sys/getCityList
    """

    url = f"{BASE_URL}/mgmt/sys/getCityList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
