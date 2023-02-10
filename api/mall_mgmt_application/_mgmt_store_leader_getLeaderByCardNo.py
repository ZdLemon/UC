# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "cardNo": "3000003480"  # str会员卡号
}

def _mgmt_store_leader_getLeaderByCardNo(params=params, access_token=access_token):
    """
    根据会员卡号获取服务中心负责人信息
    /mgmt/store/leader/getLeaderByCardNo
    """

    url = f"{BASE_URL}/mgmt/store/leader/getLeaderByCardNo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
