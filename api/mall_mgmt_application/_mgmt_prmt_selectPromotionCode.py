# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_ys

import requests


params = {
    "promotionCode": productCode_ys, # 活动编码
    "promotionId": None,
}

def _mgmt_prmt_selectPromotionCode(params=params, access_token=access_token):
    """
    查询活动编码是否已经存在
    /mgmt/prmt/selectPromotionCode
    """

    url = f"{BASE_URL}/mgmt/prmt/selectPromotionCode"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
