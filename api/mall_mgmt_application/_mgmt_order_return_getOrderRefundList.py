# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "orderNo":"", # 订单编号
    "refundTime":None, # 
    "payType":None, # 付款方式
    "creatorCard":None, # 开单人卡号
    "refundStatus":"", # 2->退款中 4->待对账校验 5->成功退款到钱包
    "financeCompanyCode":None, # 财务分公司编号
    "pageNum":1,
    "pageSize":10
}


def _mgmt_order_return_getOrderRefundList(data, access_token=access_token):
    """
    管理后台-顾客订单退款失败记录查询
    /mgmt/order/return/getOrderRefundList
    """

    url = f"{BASE_URL}/mgmt/order/return/getOrderRefundList"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
