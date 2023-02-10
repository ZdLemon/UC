# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "tradeTimeOrder": "ASC", # 支付完成时间顺序: ASC-正序,DESC-倒序,默认正序
    "companyNo":None, # 分公司编号
    "payDate": time.strftime("%Y-%m-%d",time.localtime(time.time())), # 支付日期
    "channelCode":None, # 支付渠道
    "status":None, # 平账状态
    "storeCode":None, # 服务中心编号
    "pageNum":1,
    "pageSize":10
}


def _mgmt_pay_verifyAcct_querytob(data=data, access_token=access_token):
    """
    查询对公支付对账结果信息
    /mgmt/pay/verifyAcct/querytob
    """

    url = f"{BASE_URL}/mgmt/pay/verifyAcct/querytob"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
