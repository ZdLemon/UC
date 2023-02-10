# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
	"auditRemarks": "", # 审批备注
	"auditResult": 0, # 审批结果 0不通过 1通过
	"orderId": 0 # 押货单id
}


def _mgmt_inventory_dis_mortgage_order_audit(data, access_token=access_token):
    """
    押货单审核
    /mgmt/inventory/dis/mortgage/order/audit
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/audit"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
