# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_cms_community_getCommunityCategoryList(access_token=access_token):
    """
    生活社区—查询品类列表
    /mgmt/cms/community/getCommunityCategoryList
    """

    url = f"{BASE_URL}/mgmt/cms/community/getCommunityCategoryList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
