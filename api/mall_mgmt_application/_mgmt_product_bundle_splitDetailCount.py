# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "splitId" : "",  # 拆分id
}

def _mgmt_product_bundle_splitDetailCount(params=params, access_token=access_token):
    """
    拆分明细数量统计--拆分后
    /mgmt/product/bundle/splitDetailCount
    """

    url = f"{BASE_URL}/mgmt/product/bundle/splitDetailCount"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
