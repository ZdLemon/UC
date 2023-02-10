# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
from urllib.parse import urlencode


data = {
	"splitId": "", # 拆分id
}


def _mgmt_product_bundle_splitBundle(data=data, access_token=access_token):
    """
    拆分单个套装
    /mgmt/product/bundle/splitBundle
    """

    url = f"{BASE_URL}/mgmt/product/bundle/splitBundle"
    headers = {"Authorization": f"bearer {access_token}", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
