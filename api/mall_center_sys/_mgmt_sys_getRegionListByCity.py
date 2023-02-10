# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "cityCode": "440100000000"  # str城市编码
}

def _mgmt_sys_getRegionListByCity(params=params, access_token=access_token):
    """
    根据城市编码获取下属地区
    /mgmt/sys/getRegionListByCity
    """

    url = f"{BASE_URL}/mgmt/sys/getRegionListByCity"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r