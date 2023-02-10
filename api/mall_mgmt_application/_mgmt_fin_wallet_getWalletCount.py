# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"storeCode": None, # 服务中心编号
	"cardNo": "", # 会员卡号
	"mobile": "", # 顾客手机号
	"companyCode": None, # 分公司编号
	"cardTypeList": [], # 顾客类型，1：普通顾客；2：优惠顾客；3：云商；4：微店
	"creditEnable": "", # 是否有信用额
	"negativeEnable": "", # 钱包余额为负
	"pageNum": 1,
	"pageSize": 10
}


def _mgmt_fin_wallet_getWalletCount(data=data, access_token=access_token):
    """
    获取钱包列表条数
    /mgmt/fin/wallet/getWalletCount
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getWalletCount"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
