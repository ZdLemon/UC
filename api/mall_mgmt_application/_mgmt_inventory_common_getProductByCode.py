# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "productCode": "" # 产品编号
}


def _mgmt_inventory_common_getProductByCode(params=params, access_token=access_token):
    """
    根据一或二级编码精确商品信息
    /mgmt/inventory/common/getProductByCode
    """

    url = f"{BASE_URL}/mgmt/inventory/common/getProductByCode"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
