# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time
import calendar


data = {
    "storeCode":None, # 店铺编号
    "companyCode":None, # 分公司code
    "payAccountBankName":None, # 付款银行
    "handleType":None, # 手工/自动类型 1、自动处理 2、手工处理
    "pageNum":1,
    "pageSize":10,
    "sourceType":[], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移、14->无法识别款退款、15->无法识别款不处理
    "dealType":[] # 交易类型 1、汇押货款 2、退押货款、3、其他、4、不影响押货保证金 5、押货保证金转移
}

def _mgmt_inventory_disBankRemit_pageList(data=data, access_token=access_token):
    """
    85折银行流水分页搜索列表
    /mgmt/inventory/disBankRemit/pageList
    """

    url = f"{BASE_URL}/mgmt/inventory/disBankRemit/pageList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
    
