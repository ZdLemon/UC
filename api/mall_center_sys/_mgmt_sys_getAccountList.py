# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "companyCode" : "34000",  # 公司编码
}

def _mgmt_sys_getAccountList(params=params, access_token=access_token):
    """
    查询分公司银行账号
    /mgmt/sys/getAccountList
    """

    url = f"{BASE_URL}/mgmt/sys/getAccountList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
