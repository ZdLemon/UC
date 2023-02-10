# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


def _mgmt_prmt_couponGrant_clearImportMember(access_token=access_token):
    """
    清除缓存里导入的派发用户
    /mgmt/prmt/couponGrant/clearImportMember
    """

    url = f"{BASE_URL}/mgmt/prmt/couponGrant/clearImportMember"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.post(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r))     
        return r
