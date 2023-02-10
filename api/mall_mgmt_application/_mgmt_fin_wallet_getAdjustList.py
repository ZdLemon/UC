# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"adjustStatus": None, # 审批状态：1：待审核；2：已通过；3：已驳回，6：已撤回
	"adjustMonth": None, # 录入月份
	"mobile": None, # 普通过客手机号
	"cardNo": "", # 会员卡号
	"companyCode": None, # 分公司编号
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_fin_wallet_getAdjustList(data=data, access_token=access_token):
    """
    手工录入款项审核-列表
    /mgmt/fin/wallet/getAdjustList
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getAdjustList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
