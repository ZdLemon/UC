# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "districtCode": "440105000000"  # str地区编码
}

def _mgmt_sys_getStreetListByDistrictCode(params=params, access_token=access_token):
    """
    根据地区编码获取下属街道
    /mgmt/sys/getStreetListByDistrictCode
    """

    url = f"{BASE_URL}/mgmt/sys/getStreetListByDistrictCode"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r