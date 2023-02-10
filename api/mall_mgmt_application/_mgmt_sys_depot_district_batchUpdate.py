# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "provinceCode":"110000000000", # 省编码
    "cityCode":"", # 市编码
    "sysDepotCode":"59", # 仓库编码
    "businessRange":2 # 区域
}


def _mgmt_sys_depot_district_batchUpdate(data=data, access_token=access_token):
    """
    批量修改区域对应仓库
    /mgmt/sys/depot/district/batchUpdate
    """

    url = f"{BASE_URL}/mgmt/sys/depot/district/batchUpdate"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
