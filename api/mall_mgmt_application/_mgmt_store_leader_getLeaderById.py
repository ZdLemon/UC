# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
from urllib.parse import urlencode


data = {
	"leaderId": "",
}


def _mgmt_store_leader_getLeaderById(data=data, access_token=access_token):
    """
    根据ID获取负责人信息
    /mgmt/store/leader/getLeaderById
    """

    url = f"{BASE_URL}/mgmt/store/leader/getLeaderById"
    headers = {"Authorization": f"bearer {access_token}", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
