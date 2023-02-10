# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "pageNum": 1,
    "pageSize": 10,
    "grantId": None,
    "user": None
}

def _mgmt_prmt_couponGrant_getImportMemberPage(params=params, access_token=access_token):
    """
    分页查询导入用户(导入时)
    /mgmt/prmt/couponGrant/getImportMemberPage
    """

    url = f"{BASE_URL}/mgmt/prmt/couponGrant/getImportMemberPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
