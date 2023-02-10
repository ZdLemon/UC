# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
    "feeMonth": time.strftime("%Y-%m",time.localtime(time.time())), # 月份
    "companyCode":None, # 分公司编码
    "cardNo":None, # 顾客卡号
    "feeType":None, # 手续费类型，101：微信；102：支付宝；103：银联；201：工商银行；202：建设银行；203：邮政存蓄银行；204：交通银行；205：平安代扣
    "memberType":3, # 会员类型 会员类别：1->普通顾客；2->优惠顾客；3->云商；4->微店（云+）；5->店员；6->子账号
    "pageNum":1,
    "pageSize":10
}


def _mgmt_fin_wallet_fee_queryFinWalletFee(data=data, access_token=access_token):
    """
    手续费明细表查询(商城后台)
    /mgmt/fin/wallet/fee/queryFinWalletFee
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/fee/queryFinWalletFee"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
