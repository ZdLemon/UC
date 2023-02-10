# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username_85

import requests


params = {
    "cardNo": username_85,
}

def _mgmt_prmt_selectMemberByCard(params=params, access_token=access_token):
    """
    根据会员卡号去会员中心搜索会员信息
    /mgmt/prmt/selectMemberByCard
    """

    url = f"{BASE_URL}/mgmt/prmt/selectMemberByCard"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
