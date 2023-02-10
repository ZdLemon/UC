# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username, username_85

import requests


params = {
    "cardNo": "", # 会员卡号
    "platform": None,
}

def _mobile_member_getProvideBankByCardNo(params=params, access_token=access_token):
    """
   	查询劳务发放银行卡信息
    /mobile/member/getProvideBankByCardNo
    """

    url = f"{BASE_URL}/mobile/member/getProvideBankByCardNo"
    headers = {"Authorization": f"bearer {access_token}"}

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
