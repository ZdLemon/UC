# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests


data = {
    "id":"", # 押货单id
    "auditStatus": 1, # 审核结果 0不通过 1通过
    "auditRemarks": "同意提交押货单申请" # 审核备注
}


def _mgmt_inventory_order_auditMortgageOrder(data=data, access_token=access_token):
    """
    运营后台审批押货单
    /mgmt/inventory/order/auditMortgageOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/order/auditMortgageOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
