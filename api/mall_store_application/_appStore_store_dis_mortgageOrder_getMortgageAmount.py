# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


def _appStore_store_dis_mortgageOrder_getMortgageAmount(access_token=access_token):
    """
    查询店铺押货余额与限额
    /appStore/store/dis/mortgageOrder/getMortgageAmount
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgageOrder/getMortgageAmount"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
