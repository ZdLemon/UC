# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "pageNum": 1,
    "pageSize": 10,
    "companyNo": None, # 分公司编号
    "cardNo": None, # 会员卡号
    "businessType": None, # 顾客类型：1->云商；2->微店（云+）
    "mobile": None, # 注册手机号
    "aboutMobile": None, # 关联手机号
    "status": None, # 状态：0->正常；1->异常
    "promotionType": None, # 新卡升级方式 1：产品升级 2：pv升级
    "registerMode": None, # 注册方式
    "openCardMode": None, # 开卡方式
    "selfIdCardVaildStatus": None, # 本人身份证认证状态 0：未验证; 1：已验证
    "spouseIdCardVaildStatus": None, # 配偶身份证认证状态 0：未验证; 1：已验证
    "mobileVaildStatus": None, # 手机认证状态 0：未验证; 1：已验证
    "promotionTimeStart": None, # 新卡升级时间开始
    "promotionTimeEnd":None, # 新卡升级时间结束
    "promotionTime": None, # 新卡升级时间开始
    "promotionTime":None, # 新卡升级时间结束
    "openCardTime": "1609430400000,1625068799999", # 开卡时间
    "registrationTime": None, # 转换开始时间,转换结束时间
}


def _member_mgmt_getBusinessList(params=params, access_token=access_token):
    """
    获取云商微店列表
    /member/mgmt/getBusinessList
    """

    url = f"{BASE_URL}/member/mgmt/getBusinessList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
