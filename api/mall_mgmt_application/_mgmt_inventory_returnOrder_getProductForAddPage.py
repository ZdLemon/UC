# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests


params = {
    "storeCode": store, # 服务中心编号
    "productCode": productCode, # 商品一级或二级编码
} 

def _mgmt_inventory_returnOrder_getProductForAddPage(params=params, access_token=access_token):
    """
    添加退货单时的商品搜索
    /mgmt/inventory/returnOrder/getProductForAddPage
    """

    url = f"{BASE_URL}/mgmt/inventory/returnOrder/getProductForAddPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
