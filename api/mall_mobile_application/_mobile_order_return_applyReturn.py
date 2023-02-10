# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
	"attachmentUrlList": [], # 退货凭证URL列表
	"orderNo": "", # 订单编号
	"reason1": "30天无因退货", # 退货一级原因
	"reason1Id": "1218250957143593987", # 退货一级原因id
	"reason1Remark": "" # 退货一级原因备注
}

def _mobile_order_return_applyReturn(data=data, access_token=access_token):
    """
    申请退货/退款
    /mobile/order/return/applyReturn
    """

    url = f"{BASE_URL}/mobile/order/return/applyReturn"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r



