# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "companyNo":None, # 分公司编号
    "tradeDate": time.strftime("%Y-%m-%d",time.localtime(time.time())),
    "channelCode": "", # 支付渠道
    "status":None, # 平账状态
    "cardNo":"16738855", # 会员卡号
    "memberId":None, # 顾客编号
    "pageNum":1,
    "pageSize":10
}


def _mgmt_pay_verifyAcct_query(data=data, access_token=access_token):
    """
    查询支付渠道对账结果信息
    /mgmt/pay/verifyAcct/query
    """

    url = f"{BASE_URL}/mgmt/pay/verifyAcct/query"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
