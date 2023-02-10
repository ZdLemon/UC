# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
	"storeCode": None, # 店铺编号
	"companyCode": None, # 分公司code
	"sourceType": None, # 7 手工退押货款 8 手工增押货款 9 转销售 14 钱包款与押货款互转 12 其他
	"bankName": None, # 银行名称
	"verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
	"verifyStatus": 0, # 审核状态 0 待审核 1 已审核
	"pageNum": 1,
	"pageSize": 10
}


def _mgmt_inventory_remit_pageSearchList(data=data, access_token=access_token):
    """
    手工录入流水分页搜索列表
    /mgmt/inventory/remit/pageSearchList
    """

    url = f"{BASE_URL}/mgmt/inventory/remit/pageSearchList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
