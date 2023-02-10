# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


def _mgmt_inventory_dis_mortgage_exchangeOrder_searchAuditInfo(access_token=access_token):
    """
    展示审批保存信息
    /mgmt/inventory/dis/mortgage/exchangeOrder/searchAuditInfo
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/searchAuditInfo"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
    
