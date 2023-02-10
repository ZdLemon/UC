# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


def _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(access_token=access_token):
    """
    获取启用中的拼箱费上限
    /mgmt/inventory/dis/mortgage/order/fetchPieceBoxCostCeiling
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/fetchPieceBoxCostCeiling"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
