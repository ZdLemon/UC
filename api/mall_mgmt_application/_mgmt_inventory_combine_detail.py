# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


params = {
	"id": ""
}


def _mgmt_inventory_combine_detail(params=params, access_token=access_token):
    """
    查询套装组合明细
    /mgmt/inventory/combine/detail
    """

    url = f"{BASE_URL}/mgmt/inventory/combine/detail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
