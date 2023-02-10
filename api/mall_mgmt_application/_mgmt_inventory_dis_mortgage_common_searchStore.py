# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "storeCode" : store_85,  # 服务中心编号
}

def _mgmt_inventory_dis_mortgage_common_searchStore(params=params, access_token=access_token):
    """
    查询店铺信息
    /mgmt/inventory/dis/mortgage/common/searchStore
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/common/searchStore"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
