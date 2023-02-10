# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85, storeName

import requests
from urllib.parse import urlencode


data = {
	"orderNo": "SG902804220710000063", 
}


def _appStore_orderReturn_upgradeOrderVerify(data=data, access_token=access_token):
    """
    升级单校验
    /appStore/orderReturn/upgradeOrderVerify
    """

    url = f"{BASE_URL}/appStore/orderReturn/upgradeOrderVerify"
    headers = {"Authorization": f"bearer {access_token}", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
