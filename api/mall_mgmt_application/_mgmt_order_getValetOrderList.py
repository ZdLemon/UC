# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import calendar
import time


params = {
    "customerCard": "", # 顾客会员卡
    "commitStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd HH:mm:ss"2022-05-01
    "commitEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd，当月最后一天,
    "orderStatusList": "2,3,99", # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
    "pageNum": 1,
    "pageSize": 10,
}

def _mgmt_order_getValetOrderList(params=params, access_token=access_token):
    """
    代客售后列表
    /mgmt/order/getValetOrderList
    """

    url = f"{BASE_URL}/mgmt/order/getValetOrderList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
