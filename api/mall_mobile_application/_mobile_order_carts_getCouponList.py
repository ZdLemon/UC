# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests


data = {
    "customerCard":username, # 下单人卡号
    "sourceType":1, # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整)
    "productList":[
        {
            "releList":None,
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
    ],
    "storeCode":"942437" # 服务中心编码
}

def _mobile_order_carts_getCouponList(data=data, access_token=access_token):
    """
    获取选中结算分组的可用和不可用优惠券列表
    /mobile/order/carts/getCouponList
    """

    url = f"{BASE_URL}/mobile/order/carts/getCouponList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
