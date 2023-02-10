# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "productCode": None, # 产品编号
}


def _mgmt_dis_inventory_split_forward(params=params, access_token=access_token):
    """
    拆分单个套装确认页
    /mgmt/dis-inventory/split/forward
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/split/forward"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
