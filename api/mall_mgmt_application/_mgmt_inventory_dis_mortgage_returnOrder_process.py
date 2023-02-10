# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time
import calendar


data = {
	"orderId": "227", # id
	"returnType": "2", # 退回类型 1自带 2邮寄
	"expressNo": "wmwl123456", # 物流单号
	"expressCompany": "完美物流", # 物流公司
	"expressProofUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/202204181417059OY4k.jpg",
	"expressProofName": "202204181417059OY4k.jpg", # 快递凭证名称
	"processRemark": "" # 退回处理说明
}


def _mgmt_inventory_dis_mortgage_returnOrder_process(data=data, access_token=access_token):
    """
    退回处理
    /mgmt/inventory/dis/mortgage/returnOrder/process
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/process"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
