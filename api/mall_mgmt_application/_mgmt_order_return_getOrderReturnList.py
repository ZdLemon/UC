# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time
import calendar


params = {
	"returnType": None, # 退货类型 1->当月退货 2->隔月退货
	"expressType": None, # 发货方式 1->服务中心自提 2->公司交付
	"applySource": None, # 申请来源 0->总公司代客售后 1->顾客申请 2->公司申请 3->商城1.0
	"companyCode": "", # 分公司编号
	"financeCompanyCode": "", # 财务分公司编号
	"orderDeliverStatus": None, # 订单发货状态 0->待发货 1->已发货 2->不需发货
	"storeCode": "", # 服务中心编号
	"customerCard": "", # 顾客卡号
	"creatorCard": "", # 开单人卡号
	"returnNo": "", # 退货单号
	"orderNo": "", # 订单号
	"isDeliver": None, # 是否发货 0->不发货 1->发货
	"isUpgrade": None, # 是否升级单 0->否 1->是
	"depositNo": "", # 对应定金订单号
	"currentPage": 1, 
	"pageSize": 10,
	"applyTimeBegin": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd
	"applyTimeEnd": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
	"pageNum": 1,
}

def _mgmt_order_return_getOrderReturnList(params=params, access_token=access_token):
    """
    退货单列表
    /mgmt/order/return/getOrderReturnList
    """

    url = f"{BASE_URL}/mgmt/order/return/getOrderReturnList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
