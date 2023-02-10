# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username, username_85

import requests


params = {
    "cardNo": username, # 卡号
}


def _mobile_order_before_report_cardNo(params=params, access_token=access_token):
    """
   	结算前销售调整,卡号查询是否可购买商品
    /mobile/order/before/report/{cardNo}
    """

    url = f"{BASE_URL}/mobile/order/before/report/{params['cardNo']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
