# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time
import calendar


params = {
    "applySource": None, # 申请来源 1->顾客申请 2->公司申请
    "companyCode": "", # 分公司编号
    "companyName": "", # 分公司名称
    "creatorCard": "", # 开单人卡号
    "customerCard": "", # 顾客卡号
    "expressType": None, # 配送方式 1->服务中心自提 2->公司配送
    "returnNo": "", # 退货单号
    "returnType": None, # 退货类型 1->当月退货 2->隔月退货
    "storeCode": "", # 服务中心编号
    "orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
    "currentPage": 1,
    "pageSize": 10,
    "applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
    "applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
}

def _mgmt_order_return_countWaitAudit(params=params, access_token=access_token):
    """
    统计待审核退货单
    /mgmt/order/return/countWaitAudit
    """

    url = f"{BASE_URL}/mgmt/order/return/countWaitAudit"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
