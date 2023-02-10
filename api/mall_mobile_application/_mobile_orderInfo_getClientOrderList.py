# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests
import time
import calendar


data = {
	"orderNo": "", # 订单编号
	"customerPhone": "", # 顾客手机号
	"customerCard": "", # 顾客卡号
	"customerName": "", # 顾客姓名
	"commitEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # 开单结束时间2022-04-30
	"commitStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # 开单开始时间
	"orderStatus": None, # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成 默认空为全部
	"pageNum": 1,
	"pageSize": 15,
	"total": 0,
	"serialNo": "", # 商品编码
	"title": "", # 商品名称
	"queryType": 3 # 查询类型(默认为null) null->原有订单(包含85折订单)查询 1->85折转分订单 2->85折转分补报订单 3->85折转分订单+85折转分补报订单
}

def _mobile_orderInfo_getClientOrderList(data=data, access_token=access_token):
    """
    客户端订单列表查询接口
    /mobile/orderInfo/getClientOrderList
    """

    url = f"{BASE_URL}/mobile/orderInfo/getClientOrderList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r




