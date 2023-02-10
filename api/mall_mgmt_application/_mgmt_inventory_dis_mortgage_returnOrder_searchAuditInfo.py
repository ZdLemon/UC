# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


def _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(access_token=access_token):
    """
    展示审批保存信息
    /mgmt/inventory/dis/mortgage/returnOrder/searchAuditInfo
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/searchAuditInfo"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
