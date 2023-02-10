# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "returnExpressType":1, # 退回方式 1->物流发货 2->自带
    "serviceNo":"TSG00300022071000005301", # 售后单号
    "returnExpressNo":"123456789", # 快递运单号
    "attachmentUrlList":[], # 退回凭证URL列表
    "returnExpressName":"小河物流" # 快递公司名称
}


def _mobile_web_order_return_returnGoods(data=data, access_token=access_token):
    """
    货品退回
    /mobile/web/order/return/returnGoods
    """

    url = f"{BASE_URL}/mobile/web/order/return/returnGoods"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r