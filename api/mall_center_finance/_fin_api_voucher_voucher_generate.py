# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "amount": 10,  # 金额
    "memberId": 835170191,  #  int顾客id
    "beginTime": "2022-03-01 00:00:00",
    "endTime": "2023-03-01 00:00:00",
    "num": 1
}

def _fin_api_voucher_voucher_generate(params=params, access_token=access_token):
    """
    给会员生成电子礼券，方便测试
    /fin/api/voucher/voucher/generate
    """

    url = f"{BASE_URL}/fin/api/voucher/voucher/generate"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
