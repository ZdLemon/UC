# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, username_85

import requests
import time


data = {
	"cardNo": "", # 会员卡号
	"mobile": "", # 会员手机号
	"realName": "", # 会员姓名
	"everyCount": 1, # 派发数量
	"type": 1, # 派发方式1等量2按需
	"code": "", # 使用门店
	"couponId": "" # 优惠券id
}

def _mgmt_prmt_couponGrant_addUser(data=data, access_token=access_token):
    """
    手动新增派发顾客
    /mgmt/prmt/couponGrant/addUser
    """

    url = f"{BASE_URL}/mgmt/prmt/couponGrant/addUser"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
