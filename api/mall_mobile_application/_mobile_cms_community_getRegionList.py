# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mobile_cms_community_getRegionList(access_token=access_token):
    """
    获取活动报名地区列表
    /mobile/cms/community/getRegionList
    """

    url = f"{BASE_URL}/mobile/cms/community/getRegionList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.post(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r))     
        return r
