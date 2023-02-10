# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time
import calendar


data = {
	"orderId": "", # id
	"inspectResult": "", # 验货意见 0不通过 1通过
	"expressSubsidy": "20", # 运费补贴
	"inspectRemark": "", # 验货备注
	"orderReturnRealAmount": "",
	"productList": [{ # 商品列表
		"returnRealNum": None,
		"productCode": ""
	}],
	"returnRealAmount": "" # 物品实退金额总额
}


def _mgmt_inventory_dis_mortgage_returnOrder_inspect(data=data, access_token=access_token):
    """
    验货
    /mgmt/inventory/dis/mortgage/returnOrder/inspect
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/inspect"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
