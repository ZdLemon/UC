# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "pageNum":1,
    "pageSize":10,
    "giftCouponStatus":2 # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 6:已失效 不传或者null:全部
}

def _mobile_wallet_getGiftCouponByMemberIdAndStatus(data=data, access_token=access_token):
    """
    查询电子礼券发放信息
    /mobile/wallet/getGiftCouponByMemberIdAndStatus
    """

    url = f"{BASE_URL}/mobile/wallet/getGiftCouponByMemberIdAndStatus"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r