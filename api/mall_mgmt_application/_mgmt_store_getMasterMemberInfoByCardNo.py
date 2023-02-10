# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "cardNo": "3000003480"  # str会员卡号
}

def _mgmt_store_getMasterMemberInfoByCardNo(params=params, access_token=access_token):
    """
    根据会员卡号获取主顾客信息
    /mgmt/store/getMasterMemberInfoByCardNo
    """

    url = f"{BASE_URL}/mgmt/store/getMasterMemberInfoByCardNo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
