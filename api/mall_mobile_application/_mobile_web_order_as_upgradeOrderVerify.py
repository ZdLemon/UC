# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
from urllib.parse import urlencode


data = {
	"orderNo": "SG942437220330000052", # 订单编号
}

def _mobile_web_order_as_upgradeOrderVerify(data=data, access_token=access_token):
    """
    升级单校验
    /mobile/web/order/as/upgradeOrderVerify
    """

    url = f"{BASE_URL}/mobile/web/order/as/upgradeOrderVerify"
    headers = {"Authorization": f"bearer {access_token}", "content-type": "application/x-www-form-urlencoded"}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理
  
    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r



