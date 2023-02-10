# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
    "pageNum": 1,
    "pageSize": 10,
    "companyCode": None, # 公司编码
    "principal": None, # 负责人
}


def _mgmt_sys_getComByCodeOrPri(params=params, access_token=access_token):
    """
    公司资料查询展示
    /mgmt/sys/getComByCodeOrPri
    """

    url = f"{BASE_URL}/mgmt/sys/getComByCodeOrPri"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
