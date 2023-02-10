# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"companyCode": "", # 分公司编号
	"customerCardNo": None, # 会员卡号
	"openOrderCardNo": None, # 开单人卡号
	"storeCode": None, # 服务中心编号
	"openOrderManType": None, # 开单人类型 3->云商 4->微店
	"orderType": None, # 账款类型 1->报单 ，2->退单
	"month": time.strftime("%Y%m",time.localtime(time.time())), # 月份(yyyyMM)
	"pageNum": 1,
	"pageSize": 10,
	"verifyStartDay": "", # 审核开始时间(yyyy-MM-dd)
	"verifyEndDay": "" # 审核结束时间(yyyy-MM-dd)
}

def _mgmt_inventory_transferOrder_pageList(data=data, access_token=access_token):
    """
    分页列表-85折转分分公司流水
    /mgmt/inventory/transferOrder/pageList
    """

    url = f"{BASE_URL}/mgmt/inventory/transferOrder/pageList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
