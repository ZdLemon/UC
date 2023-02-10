# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "storeCode": None, # 服务中心编码
    "companyCode": None, # 服务中心所属分公司编码
    "serialNo": None, # 产品编号
    "orderNo": None, # 订单编码
    "financeCompanyCode": None, # 订单财务分公司编码
    "pageNum": 1,
    "pageSize": 10,
    "beginDate": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01 00:00:00", # 开始时间 默认当月第一天
    "endDate": f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))} 23:59:59", # 结束时间 默认当天
}


def _mgmt_order_countOrderStoreDiffDetailByProList(params=params, access_token=access_token):
    """
    门店自提订单分公司不一致（明细表）- 按产品 统计
    /mgmt/order/countOrderStoreDiffDetailByProList
    """

    url = f"{BASE_URL}/mgmt/order/countOrderStoreDiffDetailByProList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
