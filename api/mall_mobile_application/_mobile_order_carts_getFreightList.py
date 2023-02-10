# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "customerCard": "", # 给某个顾客下单的会员卡号
    "sourceType":1, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
    "productList":[
        {
            "releList":None,
            "imgUrl":"https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png",
            "title":"玛丽艳活力精华露",
            "serialNo":"M7035", # 产品编码
            "activityPrice":480,
            "quantity":1,
            "pv":410,
            "productType":1,
            "isActivateItem":0,
            "retailPrice":480,
            "isActivity":0,
            "number":1 # 产品数量
        }
    ]
}

def _mobile_order_carts_getFreightList(data=data, access_token=access_token):
    """
    获取运费补贴券券列表
    /mobile/order/carts/getFreightList
    """

    url = f"{BASE_URL}/mobile/order/carts/getFreightList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r


