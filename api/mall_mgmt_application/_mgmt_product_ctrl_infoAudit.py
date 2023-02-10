# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "versionId":"", # 版本id
    "auditResult":1, # 审核结果 1-通过，2-不通过
    "remarks":"同意此产品通过审核" # 说明
}

def _mgmt_product_ctrl_infoAudit(data=data, access_token=access_token):
    """
    产品审核商品版本
    /mgmt/product/ctrl/infoAudit
    """

    url = f"{BASE_URL}/mgmt/product/ctrl/infoAudit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
