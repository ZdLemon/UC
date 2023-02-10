# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
	"storeCode": store_85, # 服务中心编号
}

def _mgmt_inventory_common_isStoreInTrafficControl(params=params, access_token=access_token):
    """
    店铺是否处于交通管控
    /mgmt/inventory/common/isStoreInTrafficControl
    """

    url = f"{BASE_URL}/mgmt/inventory/common/isStoreInTrafficControl"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
