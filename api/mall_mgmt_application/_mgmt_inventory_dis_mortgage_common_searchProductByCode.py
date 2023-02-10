# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "productCode": "" # 产品编号
}


def _mgmt_inventory_dis_mortgage_common_searchProductByCode(params=params, access_token=access_token):
    """
    按商品编码精确查询商品
    /mgmt/inventory/dis/mortgage/common/searchProductByCode
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/common/searchProductByCode"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
