# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "provinceCode":"", # 省编码
    "cityCode":"", # 市编码
    "districtCode":"", # 区县编码
    "businessRange":2 # 业务范围: 1.B 2.C 3.B+C
}


def _mgmt_sys_depot_district_search(data=data, access_token=access_token):
    """
    查询仓库列表
    /mgmt/sys/depot/district/search
    """

    url = f"{BASE_URL}/mgmt/sys/depot/district/search"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
