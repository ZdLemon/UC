# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "platform": 5,
    "memberId": ""
}


def _mobile_member_deletebyMemberId(params=params, access_token=access_token):
    """
    解除劳务发放银行
    /mobile/member/deletebyMemberId
    """

    url = f"{BASE_URL}/mobile/member/deletebyMemberId"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params
  
    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r