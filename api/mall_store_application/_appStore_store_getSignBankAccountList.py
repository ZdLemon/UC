# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "isSigned": 1 # 是否已签约，1/是，2/否
}

def _appStore_store_getSignBankAccountList(params=params, access_token=access_token):
    """
    获取签约银行列表
    /appStore/store/getSignBankAccountList
    """

    url = f"{BASE_URL}/appStore/store/getSignBankAccountList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
