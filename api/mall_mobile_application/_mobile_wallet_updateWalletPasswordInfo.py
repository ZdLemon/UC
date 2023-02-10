# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username

import requests


data = {
    "managerType": 3, # 支付管理类型,前端默认传值 1:设置支付密码 2:支付密码修改 3:忘记支付密码 4:关闭免密 5:开启免密
    "password":"123456", # 设置密码
    "confirmPassword":"123456", # 确认密码
    "telNum":"13982702351", # 手机号
    "smsVerificationCode":"666666" # 短信验证码
}


def _mobile_wallet_updateWalletPasswordInfo(data=data, access_token=access_token):
    """
    更新支付管理信息
    /mobile/wallet/updateWalletPasswordInfo
    """

    url = f"{BASE_URL}/mobile/wallet/updateWalletPasswordInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r