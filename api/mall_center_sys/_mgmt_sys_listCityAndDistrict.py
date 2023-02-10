# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "provinceCode": "440000000000"  # str省份编码
}

def _mgmt_sys_listCityAndDistrict(params=params, access_token=access_token):
    """
    根据省份编码获取下属城市和地区信息
    /mgmt/sys/listCityAndDistrict
    """

    url = f"{BASE_URL}/mgmt/sys/listCityAndDistrict"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r