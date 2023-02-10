# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "enclosureVos":[], # 附件集合
    "examine": None, # 审核是否通过3通过4不通过
    "grantId":"", # 优惠券派发id
    "remark":"" # 备注
}

def _mgmt_prmt_couponGrant_examineGrant(data=data, access_token=access_token):
    """
    优惠券派发审核
    /mgmt/prmt/couponGrant/examineGrant
    """

    url = f"{BASE_URL}/mgmt/prmt/couponGrant/examineGrant"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
