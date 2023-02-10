# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
	"id": None,
}


def _mgmt_sys_getComInfo(params=params, access_token=access_token):
    """
    显示company的详情
    /mgmt/sys/getComInfo
    """

    url = f"{BASE_URL}/mgmt/sys/getComInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
