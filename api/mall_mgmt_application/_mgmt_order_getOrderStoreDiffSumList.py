# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "companyCode": None, # 服务中心所属分公司编码
    "financeCompanyCode": None, # 订单财务分公司编码
    "pageNum": 1,
    "pageSize": 10,
    "beginDate": int(round(time.mktime(time.strptime(f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", '%Y-%m-%d')) * 1000)), # 开始时间 本月第一天时间戳
    "endDate": int(round(time.time() * 1000)), # 结束时间 当时时间戳
}


def _mgmt_order_getOrderStoreDiffSumList(params=params, access_token=access_token):
    """
    门店自提订单分公司不一致（汇总表）
    /mgmt/order/getOrderStoreDiffSumList
    """

    url = f"{BASE_URL}/mgmt/order/getOrderStoreDiffSumList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
