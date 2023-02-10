# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "keyword": 1, # 搜索关键字
    "pageNum": 1,
    "pageSize": 20
}

def _appStore_store_dis_mortgageOrder_searchProductPage(params=params, access_token=access_token):
    """
    关键字搜索可押货商品分页
    /appStore/store/dis/mortgageOrder/searchProductPage
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgageOrder/searchProductPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
