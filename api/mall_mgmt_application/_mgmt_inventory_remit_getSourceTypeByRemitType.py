# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "remitType": 2 # 限制平台结果累加1app2pc4小程序 # 具体银行流水类型 全部则不传 1、银行流水款项映射 2.手工录入银行流水款项映射
}

def _mgmt_inventory_remit_getSourceTypeByRemitType(params=params, access_token=access_token):
    """
    按银行流水类型获取款项映射列表
    /mgmt/inventory/remit/getSourceTypeByRemitType
    """

    url = f"{BASE_URL}/mgmt/inventory/remit/getSourceTypeByRemitType"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
