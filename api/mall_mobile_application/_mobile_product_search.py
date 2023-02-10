# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "catalogIds":[],
    "brandIds":[],
    "tagIds":[],
    "pageNum":1,
    "pageSize":12, 
    "keyword":productCode # 搜索关键字--产品名称或产品编码
}

def _mobile_product_search(data=data, access_token=access_token):
    """
    搜索商品
    /mobile/product/search
    """

    url = f"{BASE_URL}/mobile/product/search"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r

response = {
    "code":200,
    "message":"操作成功",
    "data":{
        "pageNum":1,
        "pageSize":12,
        "totalPage":1,
        "total":1,
        "list":[
            {
                "productId":"232", # 产品id
                "serialNo":"M7035", # 产品编码
                "title":"玛丽艳活力精华露",
                "catalogTitle":"化妆品(玛丽艳美容护肤品)",
                "catalogId":"3",
                "showList":[{"showId":"3","title":"化妆品 (玛丽艳美容护肤品)"}], # 前端分类集合
                "retailPrice":480.00, # 产品售价
                "underlinedPrice":480.00, # 产品划线价
                "groupPrice":374.00, # 单位团购价
                "pv":410,
                "securityPrice":160, # 押货价(订货价)
                "activityPrice":None, # 活动价
                "preDepositPrice":None, # 预售定金
                "depositDiscountPrice":None, # 定金优惠金额
                "imgUrl":"https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png",
                "orderType":1, # 订货类型 1-产品订货 2-资料订货 3-定制品订货
                "isExchangeProduct":0, # 是否换购商品 1-是，0-否
                "isPreProduct":0, # 是否预售产品 1-是，0-否
                "productType":1, # 产品类型 1-普通商品 2-定制商品 3-组合商品
                "isActivateItem":0, # 是否升级商品 1-是 0-否
                "purchaseLimitType":0, # 限购类型 0-不限购 1-终身限购 2-每月限购
                "purchaseLimitNum":None, # 限购数量
                "isIdentityLimit":0, # 是否身份限购 1-是 0-否
                "customerIdentityTypes":[0], # 会员卡限购类型 0-无限制 1-未开卡,2-未升级,3-待激活,4-有效 5-已失效
                "customerCardTypes":[0] # 身份限购类型: 0-无限制 1-会员,2-VIP会员,3-云商,4-微店
            }
        ]
    }
}