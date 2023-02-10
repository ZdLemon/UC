# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "id": None # 押货单id
}

def _appStore_store_dis_mortgageOrder_detail_id(params=params, access_token=access_token):
    """
    押货单详情
    /appStore/store/dis/mortgageOrder/detail/{id}
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgageOrder/detail/{params['id']}"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
