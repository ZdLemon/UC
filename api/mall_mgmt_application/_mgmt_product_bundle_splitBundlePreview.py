# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "productId" : "",  # 套装id
}

def _mgmt_product_bundle_splitBundlePreview(params=params, access_token=access_token):
    """
    拆分单个套装确认页
    /mgmt/product/bundle/splitBundlePreview
    """

    url = f"{BASE_URL}/mgmt/product/bundle/splitBundlePreview"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
