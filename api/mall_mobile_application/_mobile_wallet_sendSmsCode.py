# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests
import random, string


data = {
    "businessType":"1", # 业务类型 1：忘记支付密码 2:关闭免密 3:设置支付密码 4:银行卡签约 5:银行卡解约
    "phoneNum": f"189{''.join(random.sample(string.digits, 8))}"
}


def _mobile_wallet_sendSmsCode(data=data, access_token=access_token):
    """
    发送短信验证码
    /mobile/wallet/sendSmsCode
    """

    url = f"{BASE_URL}/mobile/wallet/sendSmsCode"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r