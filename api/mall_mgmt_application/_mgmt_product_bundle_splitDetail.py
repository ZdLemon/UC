# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


params = {
	"splitId": "", # 拆分id
	"pageNum": 1,
	"pageSize": 100000
}


def _mgmt_product_bundle_splitDetail(params=params, access_token=access_token):
    """
    拆分明细
    /mgmt/product/bundle/splitDetail
    """

    url = f"{BASE_URL}/mgmt/product/bundle/splitDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
