# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, store

import requests
import uuid
import time


data = {
	"returnType": 2, # 退回类型 1自带 2邮寄
	"expressCompany": "小何物流", # 物流公司
	"expressNo": str(round(time.time())), # 物流单号
	"expressFreightProof": "", # 物流费用凭证url
	"expressFreightProofName": "", # 物流费用凭证名称
	"processRemarks": "退回产品都要说明吗", # 退回处理说明
	"orderId": "" # 退货单id
}

def _appStore_purchaseReturnOrder_returnInfo(data=data, access_token=access_token):
    """
    提交退回信息
    /appStore/purchaseReturnOrder/returnInfo
    """

    url = f"{BASE_URL}/appStore/purchaseReturnOrder/returnInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
