# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "userName":"张敏",
    "companyArea":"广东",
    "regionCode":"02000",
    "contactAddress":""
}


def _mobile_cms_community_communityRegister(data=data, access_token=access_token):
    """
    活动报名
    /mobile/cms/community/communityRegister
    """

    url = f"{BASE_URL}/mobile/cms/community/communityRegister"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
