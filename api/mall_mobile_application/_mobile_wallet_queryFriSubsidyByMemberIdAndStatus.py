# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
    "pageNum":1,
    "pageSize":10,
    "giftCouponStatus":2 # 运费补贴券状态 1:已使用 2:未使用 3:占用中 4:已失效 不传或者null:全部
}


def _mobile_wallet_queryFriSubsidyByMemberIdAndStatus(data=data, access_token=access_token):
    """
    查询运费补贴券发放信息
    /mobile/wallet/queryFriSubsidyByMemberIdAndStatus
    """

    url = f"{BASE_URL}/mobile/wallet/queryFriSubsidyByMemberIdAndStatus"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
