# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"expressSubsidy": None, # 运费补贴
	"inspectRemarks": "仓库验货部门验货没问题", # 验货备注
	"inspectStatus": "1", # 验货结果 0不通过 1通过
	"orderId": "1270733832147098711", # 换货单id
	"inspectProof": ["https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706150551QvYmV.jpg", "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/202207061505569DRT2.jpg", "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220706150601mJmOV.jpg"] # 验货凭证
}


def _mgmt_inventory_exchangeOrder_inspectMortgageExchangeOrder(data, access_token=access_token):
    """
    后台押货换货单验货
    /mgmt/inventory/exchangeOrder/inspectMortgageExchangeOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/exchangeOrder/inspectMortgageExchangeOrder"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
