# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


params = {
    "showType": 1, # 显示方式：1->全部，2->当月新增（当月已购货），3->当月未购货
    "pageNum": 1,
    "pageSize": 20,
    "cardNo": None, # 会员卡号
    "mobile": None, # 手机号
    "realname": None, # 真实姓名
    "certificatesNo": None, # 证件号
    "aboutMobile": None, # 关联手机号
    "status": None, # 状态：0 启用, 1 禁用, 2 冻结, -1 已注销
    "mobileVaildStatus": None, # 手机认证状态 0：未验证; 1：已验证
    "selfIdCardVaildStatus": None, # 本人身份证认证状态 0：未验证; 1：已验证
    "spouseIdCardVaildStatus": None, # 配偶身份证认证状态 0：未验证; 1：已验证
    "channel": None, # 注册渠道：0 其他 1->H5；2->APP；3->小程序；4->PC；5->填表 6 上海健康 7 油葱极速版
    "userSource": None, # 顾客来源 1 完美商城 2 邀请注册
    "registrationTime": None, # 注册开始时间,注册结束时间
    "promotionTime": None, # 新卡升级时间 1656604800000
    "promotionTime": None, # 新卡升级时间 1659196800000
    "promotionType": None, # 新卡升级方式 1：产品升级 2：pv升级
    "registerMode": None, # 注册方式 分享产品：SHARE_PRODUCT，分享素材：SHARE_MATERIAL，分享文档：SHARE_DOCUMENT，邀请注册：INVITE_REGISTER，全程代办：FULL_AGENT，线下注册：OFFLINE_AGENT，自主注册：SELF_REGISTER
    "openCardMode": None, # 开发方式
    "openCardStartTime": 1640966400000, # 开卡时间 2022-01-01
    "openCardEndTime": 1656604799999, # 开卡时间 2022-06-30
    "promotionTimeStart": None, # 新卡升级时间开始 1656604800000
    "promotionTimeEnd": None, # 新卡升级时间结束 1659283199999
}


def _member_mgmt_getVipList(params=params, access_token=access_token):
    """
    获取优惠顾客列表
    /member/mgmt/getVipList
    """

    url = f"{BASE_URL}/member/mgmt/getVipList"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
