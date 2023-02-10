# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "storeCode": "902063"  # str服务中心编号
}

def _mgmt_store_queryStoreContractRelation(params=params, access_token=access_token):
    """
    根据服务中心编号查询服务中心合同对接关联信息
    /mgmt/store/queryStoreContractRelation
    """

    url = f"{BASE_URL}/mgmt/store/queryStoreContractRelation"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
