# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token
import requests


params = {
    "storeCode": "", # 服务中心编号
    "pageNum": 1,
    "pageSize": 10,
}


def _mgmt_store_clerk_page(params=params, access_token=access_token):
    """
    查询店员列表
    /mgmt/store/clerk/page
    """

    url = f"{BASE_URL}/mgmt/store/clerk/page"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
