# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "storeCode":"906060", # 服务中心编码（门店系统不需要填）
    "id":"510000007792" # 店员ID
}


def _mgmt_store_clerk_remove(data=data, access_token=access_token):
    """
    删除店员账号
    /mgmt/store/clerk/remove
    """

    url = f"{BASE_URL}/mgmt/store/clerk/remove"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
