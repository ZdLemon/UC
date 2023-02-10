# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import random, string, time


data = {
    "Body": {
        "WaybillRoute": [{
            "mailno": f"SF{''.join(random.sample(string.digits, 8))}",
            "acceptAddress": "test",
            "reasonName": "",
            "orderid": "我们的换货单号", # 单号，必传
            "acceptTime": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
            "remark": "test",
            "opCode": "50",
            "id": "158918741444476",
            "reasonCode": ""
        }]
    }
}

def _esb_third_sf_confirm(data=data, access_token=access_token):
    """
    顺丰物流揽件确认回调
    /esb/third/sf/confirm
    """

    url = f"{BASE_URL}/esb/third/sf/confirm"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
