# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mobile_cms_community_getUserInfo(access_token=access_token):
    """
    获取用户信息
    /mobile/cms/community/getUserInfo
    """

    url = f"{BASE_URL}/mobile/cms/community/getUserInfo"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
