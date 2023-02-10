# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_dis_inventory_settled_scope(access_token=access_token):
    """
    获取月结完成时间范围
    /mgmt/dis-inventory/settled-scope
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/settled-scope"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
    
