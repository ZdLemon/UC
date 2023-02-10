# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "storeCode":"", # 服务中心编号
    "storeName":"",
    "leaderName":"",
    "frozenTime":None, # 冻结时间
    "frozenReason":None, # 冻结原因
    "cancelTime": None, # 取消时间
    "permission":"", # 1:3押货权限
    "businessMode":1, 
    "discountPermission":"", # 85折押货权限
    "shopType": None # 权限
}


def _mgmt_store_updatePermission(data, access_token=access_token):
    """
    服务中心权限编辑修改
    /mgmt/store/updatePermission
    """

    url = f"{BASE_URL}/mgmt/store/updatePermission"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
