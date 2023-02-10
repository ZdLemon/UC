# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"expressSubsidy": 0, # 运费补贴
	"inspectRemark": "55555555555555555555", # 验货备注
	"inspectResult": "1", # 验货结果 0不通过 1通过
	"orderId": "335",
	"inspectProofUrl": ["https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220707114209GO81u.jpg", "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220707114214sIvJY.jpg", "https://test-perfect-oss-uc2.oss-cn-shenzhen.aliyuncs.com/mall-center-inventory/20220707114220XR3QM.jpg"]
}


def _mgmt_inventory_dis_mortgage_exchangeOrder_inspect(data, access_token=access_token):
    """
    验货
    /mgmt/inventory/dis/mortgage/exchangeOrder/inspect
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/exchangeOrder/inspect"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
