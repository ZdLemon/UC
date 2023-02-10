# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "sysDepotCode":"46", # 仓库编码
    "id":"1400", # 仓库区域id
    "sysDepotStatus":-1 # 状态 1：生效 -1：失效
}


def _mgmt_sys_depot_district_update(data=data, access_token=access_token):
    """
    修改区域对应仓库
    /mgmt/sys/depot/district/update
    """

    url = f"{BASE_URL}/mgmt/sys/depot/district/update"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
