# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time
import calendar


data = {
	"orderNo": "SG027000220430000055", # 订单编号
	"reason1": "其他原因退货", # 退货一级原因
	"reason1Id": "1218251042256505950", # 退货一级原因id
	"reason1Remark": "111111", # 退货一级原因备注
	"reason2": "特批退货", # 退货二级原因
	"reason2Id": "1251048643891483854", # 退货二级原因id
	"reason2Remark": "222222", # 退货二级原因备注
	"applySource": 0 # 来源 0->总公司代客申请 1->顾客申请 2->公司申请
}


def _mgmt_order_return_applyReturn(data=data, access_token=access_token):
    """
    申请退货
    /mgmt/order/return/applyReturn
    """

    url = f"{BASE_URL}/mgmt/order/return/applyReturn"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
