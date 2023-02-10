# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber

import requests


def _mgmt_prmt_coupon_getShowList(access_token=access_token):
    """
    商品分类列表
    /mgmt/prmt/coupon/getShowList
    """

    url = f"{BASE_URL}/mgmt/prmt/coupon/getShowList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
