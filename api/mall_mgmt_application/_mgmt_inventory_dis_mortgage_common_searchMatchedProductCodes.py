# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "productCode": "" # 产品编号
}


def _mgmt_inventory_dis_mortgage_common_searchMatchedProductCodes(params=params, access_token=access_token):
    """
    获取所有匹配的商品编码列表
    /mgmt/inventory/dis/mortgage/common/searchMatchedProductCodes
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/common/searchMatchedProductCodes"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
