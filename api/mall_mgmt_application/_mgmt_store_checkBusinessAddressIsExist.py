# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "provinceName": "广东省",  # 省份
    "cityName": "广州市",  # 城市
    "areaName": "海珠区",  # 区县
    "streetName": "南洲街道",  # 街道
    "detailAddress": "广州市海珠区南洲街道新滘中路88号唯品同创汇6区东三街17号自编23号"  #服务中心详细地址(门牌号)
}

def _mgmt_store_checkBusinessAddressIsExist(params=params, access_token=access_token):
    """
    检查经营地址是否存在，返回重复的服务中心编码，返回空则表示无重复
    /mgmt/store/checkBusinessAddressIsExist
    """

    url = f"{BASE_URL}/mgmt/store/checkBusinessAddressIsExist"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
