# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "orderId" : None,  # 押货单id
}

def _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params=params, access_token=access_token):
    """
    查询押货单是否超出库存限额
    /mgmt/inventory/dis/mortgage/order/checkIsAuditAmountOverLimit
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/checkIsAuditAmountOverLimit"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
