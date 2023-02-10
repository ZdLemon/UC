# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "memberType" : 3,  # int 负责人会员类型
    "storeName" : "" #str 服务中心名称
}

def _mgmt_store_checkStoreNameIsExist(params=params, access_token=access_token):
    """
    检查服务中心名称是否存在, code=500时,存在相同值,提示语取message
    /mgmt/store/checkStoreNameIsExist
    """

    url = f"{BASE_URL}/mgmt/store/checkStoreNameIsExist"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
