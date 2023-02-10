# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"orderId": "333", # 换货单id
	"expressAmount": 0, # 物流金额
	"expressCompany": "", # 快递公司
	"expressNo": "", # 快递单号
	"expressProofUrl": "", # 快递凭证url
	"expressProofName": "", # 快递凭证名称
	"processRemark": "4444444444444444", # 退回说明
	"returnType": "1", # 退回方式 1服务中心报废 2自带 3邮寄
	"disposalProofName": "20220707112432CK443.jpg,20220707112433WL1iH.jpg,20220707112437lf3fT.jpg", # 报废凭证名称,最多9个，逗号隔开
	"disposalProofUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220707112432CK443.jpg,https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220707112433WL1iH.jpg,https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220707112437lf3fT.jpg" # 报废凭证,最多9个，逗号隔开
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_process(data=data, access_token=access_token):
    """
    退回
    /mgmt/inventory/dis/mortgage/exchangeOrder/process
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/process"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
