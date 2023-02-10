# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "versionId":"", # 商品版本id
    "pageNum":1,
    "pageSize":20,
    "operator":None, # 操作人
    "auditTypeResult":None # 审核意见 0-全部，1-产品审核通过，2-产品审核不通过，3-财务审核通过，4-财务审核不通过
}

def _mgmt_product_ctrl_listAuditLog(data=data, access_token=access_token):
    """
    商品版本审核历史列表
    /mgmt/product/ctrl/listAuditLog
    """

    url = f"{BASE_URL}/mgmt/product/ctrl/listAuditLog"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
