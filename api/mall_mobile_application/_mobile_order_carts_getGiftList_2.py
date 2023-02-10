# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests


data = {
    "customerCard":username,
    "sourceType":1,
    "productList":[
        {"releList":None,
         "imgUrl":"https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png",
         "title":"玛丽艳活力精华露",
         "serialNo":"M7035",
         "activityPrice":480,
         "quantity":1,
         "pv":410,
         "productType":1,
         "isActivateItem":0,
         "retailPrice":480,
         "isActivity":0,
         "number":1
        }
    ]
}


def _mobile_order_carts_getGiftList_2(data=data, access_token=access_token):
    """
    获取电子礼券列表
    /mobile/order/carts/getGiftList/2.2
    """

    url = f"{BASE_URL}/mobile/order/carts/getGiftList/2.2"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
