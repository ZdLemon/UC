# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "orderNo": "", # 订单编号
}


def _mgmt_order_as_applyAfterSale(params=params, access_token=access_token):
    """
    申请售后是否支持退货、换货
    /mgmt/order/as/applyAfterSale
    """

    url = f"{BASE_URL}/mgmt/order/as/applyAfterSale"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
