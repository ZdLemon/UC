# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


params = {
    "productId": 232, # 当前商品id
}

def _mobile_myShareAndFavorite_whetherAddFavPro(params=params, access_token=access_token):
    """
    判断该商品是否被此会员收藏
    /mobile/myShareAndFavorite/whetherAddFavPro
    """

    url = f"{BASE_URL}/mobile/myShareAndFavorite/whetherAddFavPro"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r

