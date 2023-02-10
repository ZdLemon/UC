# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


params = {
    "orderStatus": None, # 处理状态 1待审核 2待退回 3待验货 4已完成 5已取消
    "pageNum": 1,
    "pageSize": 10,
    "beginTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # 申请开始日期2022-04-01
    "companyCode": None,
    "endTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}', # 申请结束日期
    "orderSn": None, # 退货单编号
    "orderSource": None, # 押货单来源 1服务中心押货 2运营后台押货
    "storeCode": None, # 服务中心编号
    "orderMark": None # 退货标识 1普通押货退货 2套装组合退货 3套装拆分退货 4押货修改退
}

def _mgmt_inventory_dis_mortgage_returnOrder_listPage(params=params, access_token=access_token):
    """
    押货退货分页列表
    /mgmt/inventory/dis/mortgage/returnOrder/listPage
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/listPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
