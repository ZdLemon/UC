# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "bindName":"孟光", # 签约人姓名
    "bindIdcard":"220125197102160060", # 签约人身份证号
    "bankType":"ICBC", # 银行类别，ICBC：工商银行 PSBC：邮政储蓄银行
    "bankAccount":"622123456789963", # 银行账号
    "tel":"18928790145",
    "smsCode":"666666",
    "maincardSpouse": 0 # 是否主卡或配偶 0：主卡 1：配偶
}


def _mobile_wallet_signBankCard(data=data, access_token=access_token):
    """
    签约银行卡
    /mobile/wallet/signBankCard
    """

    url = f"{BASE_URL}/mobile/wallet/signBankCard"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r



