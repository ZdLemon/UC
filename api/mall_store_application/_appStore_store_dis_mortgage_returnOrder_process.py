# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store_85

import requests
import uuid
import time


data = {
	"returnType": "1", # 退回类型 1自带 2邮寄
	"expressCompany": "", # 物流公司
	"expressNo": "", # 物流单号
	"expressProofUrl": "", # 快递凭证url
	"expressProofName": "", # 快递凭证名称
	"processRemark": "", # 退回处理说明
	"orderId": "366" # 退货单id
}

def _appStore_store_dis_mortgage_returnOrder_process(data=data, access_token=access_token):
    """
    退回处理
    /appStore/store/dis/mortgage/returnOrder/process
    """

    url = f"{BASE_URL}/appStore/store/dis/mortgage/returnOrder/process"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
