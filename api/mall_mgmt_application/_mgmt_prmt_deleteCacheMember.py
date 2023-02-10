# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber

import requests

data = {
	"id": None
}

def _mgmt_prmt_deleteCacheMember(data=data, access_token=access_token):
    """
    删除缓存的活动用户
    /mgmt/prmt/deleteCacheMember
    """

    url = f"{BASE_URL}/mgmt/prmt/deleteCacheMember"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
