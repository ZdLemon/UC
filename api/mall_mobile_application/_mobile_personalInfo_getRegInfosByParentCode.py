# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "parentCode": 0, # 该地区的父编码,不传默认值时默获取省的信息，(使用于多级联动的效果) 省的parentCode默认为0
}

def _mobile_personalInfo_getRegInfosByParentCode(params=params, access_token=access_token):
    """
    通过传parentCode获得相应的区域信息
    /mobile/personalInfo/getRegInfosByParentCode
    """

    url = f"{BASE_URL}/mobile/personalInfo/getRegInfosByParentCode"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
