# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests
import time
import calendar


params = {
    "storeCode": store, # 服务中心编号
    "productCode": productCode, # 产品编码
    "beginMonth": "",
    "endMonth": ""
}

def _mgmt_inventory_book_items(params=params, access_token=access_token):
    """
    查询实时库存台账明细
    /mgmt/inventory/book-items
    """

    url = f"{BASE_URL}/mgmt/inventory/book-items"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r


response = {
        "code":200,
        "message":"操作成功",
        "data":[
            {
                "businessId":"SG902804220519002642", # 来源的 业务id （可能是押货id，可能是商城订单id）
                "diffNum":-2, # 增减值
                "source":3, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                "outIn":2 # 出入库：1入库 2出库
            }
        ]
}
