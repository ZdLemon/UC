# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username, username_85

import requests


params = {
    "cardNo": username, # 顾客卡号
}

def _mobile_order_before_by_cardNo(params=params, access_token=access_token):
    """
    根据用户卡号查询是否可购买商品
    /mobile/order/before/by/{cardNo}
    """

    url = f"{BASE_URL}/mobile/order/before/by/{params['cardNo']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r


response = {
	"code": 200,
	"message": "操作成功",
	"data": {
		"id": "814498218",
		"cardNo": "14498218",
		"nickname": None,
		"realname": "李哲",
		"pv": 54671.00,
		"lastOrderTime": "2021.04", # 调整时间
		"adjustTime": "2022-03", # 调整时间
		"gifPrice": 40.00, # 电子礼券金额
		"currentGifPrice": 40.00, # 当前可用电子礼券金额
		"isFiveStar": 1,
		"cardStatus": 0, # 卡状态：-3->未开卡；-2->未激活；-1->待激活；0->有效；1->已失效；2->已注销
		"cancelDate": None, # 取消月份
		"orderWay": 1 # 下单方式 1-自购,2-代购
	}
}