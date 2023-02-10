# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, couponNumber

import requests

data = {
	"promotionId": "", # 活动id
	"examine": None, # 审核是否通过3通过4不通过
	"remarks": "", # 备注
	"enclosureVos": [] # 附件集合
}

def _mgmt_prmt_promotionExamine(data=data, access_token=access_token):
    """
    活动审核
    /mgmt/prmt/promotionExamine
    """

    url = f"{BASE_URL}/mgmt/prmt/promotionExamine"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
