# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "serviceNo": "TSG00300022071000005301", # 售后单号
    "auditStatus": "1", # 审核状态 1->通过 2->不通过
    "remarks": "同意", # 审核意见
    "attachmentUrlList": [], # 审核附件URL列表
    "subsidyFreight": "20" # 运费补贴
}


def _mgmt_order_return_auditGoods(data=data, access_token=access_token):
    """
    退货验货审核
    /mgmt/order/return/auditGoods
    """

    url = f"{BASE_URL}/mgmt/order/return/auditGoods"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r