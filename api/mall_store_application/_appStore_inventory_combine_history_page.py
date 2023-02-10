# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode_zh

import requests


params = {
    "pageNum": 1,
    "pageSize": 20,
    "beginTime": "", # 开始时间
    "endTime": "" # 结束时间
}

def _appStore_inventory_combine_history_page(params=params, access_token=access_token):
    """
    套装组合记录列表
    /appStore/inventory/combine/history/page
    """

    url = f"{BASE_URL}/appStore/inventory/combine/history/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
