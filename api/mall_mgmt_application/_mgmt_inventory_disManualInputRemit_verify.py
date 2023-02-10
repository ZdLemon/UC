# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "id": None, # 主键id
    "verifyRemark": "", # 审核备注
    "verifyResult": None # 1->通过 2-> 拒绝
}

def _mgmt_inventory_disManualInputRemit_verify(params=params, access_token=access_token):
    """
    85折手工录入流水单个审核
    /mgmt/inventory/disManualInputRemit/verify
    """

    url = f"{BASE_URL}/mgmt/inventory/disManualInputRemit/verify"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
