# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "productIds" : "",  # 套装id
}

def _mgmt_product_bundle_splitPreview(params=params, access_token=access_token):
    """
    批量/单独拆分前明细预览
    /mgmt/product/bundle/splitPreview
    """

    url = f"{BASE_URL}/mgmt/product/bundle/splitPreview"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
