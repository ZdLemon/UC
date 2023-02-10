# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests


data = {
    "productDtoList":[ # 需要修改的商品
        {
            "productCode": productCode, # 商品一级编码
            "productSecCode":"", # 商品二级编码(非定制品不要传此字段)
            "productNum":1 # 需要减少的商品数量(绝对值)
        }
    ],
    "storeCode": store # 店铺中心编号
}


def _mgmt_inventory_order_checkProductInventory(data=data, access_token=access_token):
    """
    店铺库存校验接口
    /mgmt/inventory/order/checkProductInventory
    """

    url = f"{BASE_URL}/mgmt/inventory/order/checkProductInventory"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
