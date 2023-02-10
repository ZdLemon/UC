# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode, username

import requests


params = {
	"withdrawId": None # 主键
}

def _mobile_wallet_querySecondCouponWithdrawdtlList(params=params, access_token=access_token):
    """
    秒返券提现详情查询
    /mobile/wallet/querySecondCouponWithdrawdtlList
    """

    url = f"{BASE_URL}/mobile/wallet/querySecondCouponWithdrawdtlList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params
  
    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
