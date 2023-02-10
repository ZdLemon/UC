# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "type": None, # 类型：1冻结 2解冻
    "bizType": None, # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
    "beginMonth": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
    "endMonth": time.strftime("%Y%m",time.localtime(time.time())), # 202204月份，格式为：yyyyMM
    "monthTime": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
    "monthTime": time.strftime("%Y%m",time.localtime(time.time())), #202204月份，格式为：yyyyMM
	"storeCode": store_85, # 服务中心编号
	"productCode": productCode, # 产品编号
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_dis_inventory_frozen_detail(params=params, access_token=access_token):
    """
    查询库存冻结明细
    /mgmt/dis-inventory/frozen-detail
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/frozen-detail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
