# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "orderNo": "SG942437220329000036", # 订单号
}

def _mobile_web_order_as_applyAfterSale(params=params, access_token=access_token):
    """
    申请售后是否支持退货、换货、维修、返修
    /mobile/web/order/as/applyAfterSale
    """

    url = f"{BASE_URL}/mobile/web/order/as/applyAfterSale"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
