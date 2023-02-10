# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests


params = {
    "storeCode": store_85, # 服务中心编号
    "productCode": productCode, # 产品编码
    "beginMonth": "",
    "endMonth": ""
}

def _mgmt_dis_inventory_book_items(params=params, access_token=access_token):
    """
    查询实时库存台账明细
    /mgmt/dis-inventory/book-items
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/book-items"
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
                "bizNo": "YH8590220822050554", # 来源的 业务id （可能是押货id，可能是商城订单id）
                "diffNum": 2, # 增减值
                "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                "type": 1 # 出入库：1入库 2出库
            }
        ]
}
