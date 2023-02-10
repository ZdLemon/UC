# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber

import requests

data = {
    "serviceNo":"DTSG90426922072700110301", # 售后单号
    "auditStatus":"1", # 审核状态 1->通过 2->不通过
    "remarks":"同意退款" # 审核意见
}


def _mgmt_order_return_auditOrderReturn(data=data, access_token=access_token):
    """
    分公司退货审核
    /mgmt/order/return/auditOrderReturn
    """

    url = f"{BASE_URL}/mgmt/order/return/auditOrderReturn"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
