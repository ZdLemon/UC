# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "id": "", # ID，主账号传会员ID，子账号传子账号ID
}


def _member_mgmt_resetMemberPassword(data=data, access_token=access_token):
    """
    重置会员密码
    /member/mgmt/resetMemberPassword
    """

    url = f"{BASE_URL}/member/mgmt/resetMemberPassword"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
