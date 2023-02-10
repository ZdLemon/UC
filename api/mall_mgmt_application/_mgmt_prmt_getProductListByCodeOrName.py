# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "id": None, # 活动id
    "type": None, # 搜索来源:1活动 2换购 3加购 4预售 null优惠券
    "productCode": "", # 产品编码
}

def _mgmt_prmt_getProductListByCodeOrName(params=params, access_token=access_token):
    """
    根据产品编码或名称搜索产品（新建活动）
    /mgmt/prmt/getProductListByCodeOrName
    """

    url = f"{BASE_URL}/mgmt/prmt/getProductListByCodeOrName"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
