# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": None, # 店铺编号
	"companyCode": None, # 分公司code
	"bankName": None, # 银行名称 -- 不传则全部
	"sysTime": None,
	"dealStatus": 0, # 处理状态 0 待处理 1 已处理 2 -> 不处理
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_inventory_remit_unknownRemit_pageList(data=data, access_token=access_token):
    """
    未知款项流水分页搜索列表
    /mgmt/inventory/remit/unknownRemit/pageList
    """

    url = f"{BASE_URL}/mgmt/inventory/remit/unknownRemit/pageList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
