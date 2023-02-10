# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
	"productCodes": []
}


def _mgmt_dis_inventory_split(data=data, access_token=access_token):
    """
    套装拆分
    /mgmt/dis-inventory/split
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/split"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
