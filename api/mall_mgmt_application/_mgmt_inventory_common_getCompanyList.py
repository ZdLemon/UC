# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


def _mgmt_inventory_common_getCompanyList(access_token=access_token):
    """
    获取分公司列表
    /mgmt/inventory/common/getCompanyList
    """

    url = f"{BASE_URL}/mgmt/inventory/common/getCompanyList"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
