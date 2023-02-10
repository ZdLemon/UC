# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85, storeName

import requests


data = {
    "auditStatus":"1", # 审核状态 1->通过 2->不通过
    "remarks": "2222222222222222222222", # 备注
    "getStatus": 1,
    "serviceNo": "TSG90280422071000006301" # 售后单号
}


def _appStore_orderReturn_audit(data=data, access_token=access_token):
    """
    售后单审核
    /appStore/orderReturn/audit
    """

    url = f"{BASE_URL}/appStore/orderReturn/audit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
