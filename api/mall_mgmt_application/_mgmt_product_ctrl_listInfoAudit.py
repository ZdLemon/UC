# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"auditStauts": "1", # 审核状态 1-所有，2-待审核，3-已通过，4-未通过
	"pageNum": 1,
	"pageSize": 10,
	"serialNo": "", # 商品编码
	"title": None,
	"startTime": "", # 开始时间时间戳 1648742400000,本月第一天
	"endTime": "" # 结束时间时间戳,本月当天
}

def _mgmt_product_ctrl_listInfoAudit(data=data, access_token=access_token):
    """
    待产品审核商品版本列表
    /mgmt/product/ctrl/listInfoAudit
    """

    url = f"{BASE_URL}/mgmt/product/ctrl/listInfoAudit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
