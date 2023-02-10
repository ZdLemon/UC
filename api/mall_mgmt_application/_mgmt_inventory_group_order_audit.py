# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


data = {
    "attachments":[], # 审核附件
    "auditResult": None, # 审核结果：0、不通过 1、通过
    "auditView":"", # 审核意见
    "orderNo":"" # 订单编号
}

def _mgmt_inventory_group_order_audit(data=data, access_token=access_token):
    """
    审核团购单
    /mgmt/inventory/group-order/audit
    """

    url = f"{BASE_URL}/mgmt/inventory/group-order/audit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.put(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
    
