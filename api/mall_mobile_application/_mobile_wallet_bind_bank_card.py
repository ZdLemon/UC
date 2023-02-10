# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests


data = {
    "bindName":"证件啦啦啦", # 绑定人姓名
    "bindIdcard":"22222", # 绑定人身份证
    "bankName":"中国银行", # 银行名称
    "bankCode":"01", # 银行编码
    "bankAccount":"622123654789", # 银行账号
    "bankProvinceCode":"110000000000", # 银行所属省编码
    "bankCityCode":"110100000000", # 银行所属市编码
    "province":"北京市", # 银行省
    "city":"北京市", # 银行市
    "bankBranchName":"解放路支行", # 开户行名称
    "maincardSpouse":0, # 是否主卡或配偶 0：主卡 1：配偶
    "labourBankAccount":1 # 劳务收入账号类型 0:劳务绑定 1:非劳务绑定
}


def _mobile_wallet_bind_bank_card(data=data, access_token=access_token):
    """
    绑定银行卡
    /mobile/wallet/bind/bank/card
    """

    url = f"{BASE_URL}/mobile/wallet/bind/bank/card"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r

