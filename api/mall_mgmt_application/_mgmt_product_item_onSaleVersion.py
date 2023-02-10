# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
	"productId": ""
}

def _mgmt_product_item_onSaleVersion(params=params, access_token=access_token):
    """
    商品版本上架
    /mgmt/product/item/onSaleVersion
    """

    url = f"{BASE_URL}/mgmt/product/item/onSaleVersion"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.post(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
