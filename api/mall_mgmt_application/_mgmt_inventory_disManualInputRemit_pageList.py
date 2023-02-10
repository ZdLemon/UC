# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"monthrange": None,
	"storeCode": "", # 店铺编号
	"companyCode": None, # 分公司code
	"sourceType": None, # 款项类型 3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
	"payAccountBankName": None, # 付款银行
	"verifyResult": None, # 审核结果 0未审核 1通过 2拒绝
	"verifyStatus": 0, # 审核状态 0 待审核 1 已审核
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_inventory_disManualInputRemit_pageList(data=data, access_token=access_token):
    """
    85折手工录入流水分页搜索列表
    /mgmt/inventory/disManualInputRemit/pageList
    """

    url = f"{BASE_URL}/mgmt/inventory/disManualInputRemit/pageList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
