# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
	"payOrderNo": "",
}

def _pay_notify_mockPaySuccess(params=params, access_token=access_token):
    """
    银联支付回调
    /pay/notify/mockPaySuccess
    """

    url = f"{BASE_URL}/pay/notify/mockPaySuccess"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params
  
    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
