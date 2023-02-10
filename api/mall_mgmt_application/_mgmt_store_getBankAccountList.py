# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "storeCode" : store_85,  # 服务中心编号
}

def _mgmt_store_getBankAccountList(params=params, access_token=access_token):
    """
    通过storeCode获取银行账户资料信息
    /mgmt/store/getBankAccountList
    """

    url = f"{BASE_URL}/mgmt/store/getBankAccountList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
