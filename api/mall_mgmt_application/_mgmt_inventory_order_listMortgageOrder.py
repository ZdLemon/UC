# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store, productCode

import requests
import time
import calendar


params = {
    "orderStatus": None, # 押货单状态,1待审核 2待发货（审核通过） 3部分发货 4已完成 5已取消
    "pageNum": 1,
    "pageSize": 10,
    "beginTime": "", # yyyy-MM-dd 
    "companyCode": "", # 所属分公司编号
    "endTime": "",
    "orderMark": None, # 标志 1普通押货单 2仅调账不发货 3套装组合押货 4套装拆分押货
    "orderSn": "", # 押货单号
    "orderSource": None, # 押货单来源 1服务中心押货 2运营后台押货
    "storeCode": "", # 服务中心编号
    "editFlag": None, # 是否有修改过 0未修改 1已修改
    "customFlag": None, # 是否有为定制品押货单 0不是 1是
    "isTrafficControl": None # 是否交通管制 0否 1是
}


def _mgmt_inventory_order_listMortgageOrder(params=params, access_token=access_token):
    """
    运营后台押货单列表查询
    /mgmt/inventory/order/listMortgageOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/order/listMortgageOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
