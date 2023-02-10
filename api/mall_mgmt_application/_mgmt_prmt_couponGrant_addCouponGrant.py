# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"type": 1, # 导入方式1等量派发2按需派发
	"grantType": 1, # 派发方式1即时派发2定时派发3每日循环派发4每月定时派发
	"grantTarget": 4, # 派发对象1所有人2身份3等级4导入
	"everyCount": 1, # 每人发放数量
	"fixedTime": "", # 定时派发时间(yyyy-MM-dd HH:mm:ss)
	"grantStartTime": None, # 定时派发开始时间(yyyy-MM-dd HH:mm:ss)
	"grantEndTime": None, # 定时派发结束时间(yyyy-MM-dd HH:mm:ss)
	"memberIdentities": [], # 用户身份集合
	"memberLevelList": [], # 顾客等级:0.新用户,1.一星优惠客户,2.二星优惠客户,3.三星优惠客户,4.四星优惠客户,5.客户代表,6.客户经理,7.中级客户经理,8.客户总监,9.高级客户总监,10.资深客户总监,11.客户总经理
	"cardStatuses": [], # 会员卡状态:-3.未开卡,-2.未升级,-1.待激活,0.有效,1.已失效,2.已注销
	"limitMemberLevel": False, # 是否限制顾客等级
	"limitOrderTime": 0, # 限制购货月份:0-不限制,1-限制,2-从未购货
	"limitCardTime": 0, # 是否限制开卡时间0否1是2限制注册时间
	"limitRegTime": 0, # 是否限制注册月份:0-不限制,1-限制
	"startTime": None, # 开卡时间起(yyyy-MM)
	"endTime": None, # endTime
	"regStartTime": None, # 注册月份起区(yyyy-MM)
	"regEndTime": None, # 注册月份止区(yyyy-MM)
	"orderStartTime": None, # 购货月份起区(yyyy-MM)
	"orderEndTime": None, # 购货月份止区(yyyy-MM)
	"couponId": "1270722876147919236", # 优惠券id
	"state": 1 # 发放状态1待审核2派发中3已完成4已驳回5草稿
}

def _mgmt_prmt_couponGrant_addCouponGrant(data=data, access_token=access_token):
    """
    新增优惠券派发记录
    /mgmt/prmt/couponGrant/addCouponGrant
    """

    url = f"{BASE_URL}/mgmt/prmt/couponGrant/addCouponGrant"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
