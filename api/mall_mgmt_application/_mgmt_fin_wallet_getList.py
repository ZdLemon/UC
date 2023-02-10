# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": None,
	"cardNo": None, # 会员卡号
	"mobile": None, # 顾客手机号
	"companyCode": None, # 	分公司编号
	"cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
	"creditEnable": None, # 是否有信用额
	"negativeEnable": None, # 钱包余额为负
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_fin_wallet_getList(data=data, access_token=access_token):
    """
    完美钱包管理-列表
    /mgmt/fin/wallet/getList
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
