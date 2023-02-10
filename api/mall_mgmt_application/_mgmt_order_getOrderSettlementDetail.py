# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


params = {
	"orderMonth": time.strftime("%Y%m",time.localtime(time.time())), # 业绩月份202204
	"storeCode": store_85, # 服务中心编号
	"orderNo": "", # 订单编号/售后单号
    "orderType": None, # 订单类型 1->商城报单 2->商城退单
    "isDifference": None, # 交付差额是否为负 0->否 1->是
	"tradingStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # 交易开始时间2022-04-01
	"tradingEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # 交易结束时间
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_order_getOrderSettlementDetail(params=params, access_token=access_token):
    """
    交付结算详情
    /mgmt/order/getOrderSettlementDetail
    """

    url = f"{BASE_URL}/mgmt/order/getOrderSettlementDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
