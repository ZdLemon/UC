# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests
import time
import calendar


params = {
    "orderStatus": None, # 处理状态 1待审核 2待退回 3待验货 4已完成 5已取消
    "pageNum": 1,
    "pageSize": 10,
    "beginTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd 
    "companyCode": "", # 所属分公司编号
    "endTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # yyyy-MM-dd 当月最后一天
    "orderMark": None, # 押货退货单标识 1普通押货退货 2套装组合退货 3套装拆分退货 4押货修改退
    "orderSn": "", # 押货退货单号
    "orderSource": None, # 退货单来源 1服务中心退货 2运营后台退货
    "storeCode": "", # 服务中心编号
}


def _mgmt_inventory_returnOrder_listOrder(params=params, access_token=access_token):
    """
    后台查询押货退货单列表
    /mgmt/inventory/returnOrder/listOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/returnOrder/listOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
