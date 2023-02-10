# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "type": "openBankCode", # 开户银行type为openBankCode，注销原因和审核不通过原因暂无
}


def _crm_member_serviceCompany_bankOfDeposit(params=params, access_token=access_token):
    """
    注销原因、审核不通过原因、开户银行接口
    /crm/member/serviceCompany/bankOfDeposit
    """

    url = f"{BASE_URL}/crm/member/serviceCompany/bankOfDeposit"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
