# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


def _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(access_token=access_token):
    """
    获取最新的运费计算模板
    /mgmt/inventory/dis/mortgage/common/fetchFreightTemplate
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/common/fetchFreightTemplate"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r))     
        return r
