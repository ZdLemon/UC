# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"orderId": "1270733832147098709", # 换货单id
	"expressAmount": 0, # 物流金额
	"expressCompany": "", # 快递公司
	"expressNo": "", # 快递单号
	"expressProofUrl": "", # 快递凭证url
	"expressProofName": "", # 快递凭证名称
	"processRemarks": "这是我的报废图片", # 退回说明
	"returnType": 1, # 退回方式 1服务中心报废 2自带 3邮寄
	"disposalProofName": "20220706144452VWNqW.jpg,20220706144458pZaoz.jpg,20220706144503yhVnc.jpg", # 报废凭证名称,最多9个，逗号隔开
	"disposalProofUrl": "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706144452VWNqW.jpg,https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706144458pZaoz.jpg,https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706144503yhVnc.jpg" # 报废凭证,最多9个，逗号隔开
}


def _mgmt_inventory_exchangeOrder_processMortgageExchangeOrder(data, access_token=access_token):
    """
    后台押货换货单退回处理
    /mgmt/inventory/exchangeOrder/processMortgageExchangeOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/processMortgageExchangeOrder"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
