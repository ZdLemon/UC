# coding:utf-8

from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口

from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_queryList import _mgmt_fin_voucher_second_coupon_queryList # 秒返券列表
from api.mall_mgmt_application._mgmt_fin_voucher_second_coupon_updateWithdrawconf import _mgmt_fin_voucher_second_coupon_updateWithdrawconf # 秒返券提现配置修改
from api.mall_mobile_application._mobile_wallet_applySecondCouponWithdraw import _mobile_wallet_applySecondCouponWithdraw # 秒返券申请提现

 
from setting import USERNAME02, username, name, username_vip, name_vip, store, store_85, productCode_02, username_85, store13, store85, productCode_SecondCoupon, couponNumber
from util.stepreruns import stepreruns
import os
from copy import deepcopy
import pytest
import time
import allure
import random, string
from datetime import date, timedelta
import calendar


# 提现状态流转

@allure.title("VIP顾客订单-提现待审核：秒返券提现中")
@pytest.fixture(scope="package", autouse=True)
def vip_Second_2_7(vip_login_2):
        
    getCurrentUserInfo = None # 个人用户信息
    getSecondList = None # 秒返券
    token = os.environ["vip_token_2"]
    access_token = os.environ["access_token_2"]
    
    @allure.step("个人用户信息")
    def step_mobile_personalInfo_getCurrentUserInfo():

        nonlocal getCurrentUserInfo
        with _mobile_personalInfo_getCurrentUserInfo(token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCurrentUserInfo = r.json()["data"]

    @allure.step("秒返券提现配置修改")
    def step_mgmt_fin_voucher_second_coupon_updateWithdrawconf():
        
        data = {
            "id": 1,
            "maxNum": 100, # 每月提现次数上限
            "minAmount": 1, # 单次提现合计金额下限
            "remark": """
        
        1. 指由于来源订单提交售后，需锁定未使用的购物秒返券，不允许顾客继续下单
        2. 来源订单提交售后后：
            a、此订单关联的未使用购物秒返券需锁定
            b、已使用、占用中、提现中的购物秒返券不需处理。若此类购物秒返券释放回未使用状态时，也需锁定
        
        3.1.0需求：
        拆券派发：购物秒返券最大面额为300元，超过300元需拆成多张发放
        1. 单张订单产生的购物秒返券大于等于300元，则拆成300元/张派发给用户，剩余不足300元的合成一张发放
        2. 单张订单产生的购物秒返券小于300元，直接发放一张即可
        """ # 提现说明
        }
        
        with _mgmt_fin_voucher_second_coupon_updateWithdrawconf(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
 
    @allure.step("秒返券列表")    
    def step_mgmt_fin_voucher_second_coupon_queryList():

        nonlocal getSecondList
        data = {
            "cardNo": getCurrentUserInfo["cardNo"],
            "mobile":None,
            "memberType":None,
            "sourceOrderNo":"",
            "withdrawBatch":None,
            "sourceStoreCode":None,
            "couponStatusList": [2], # 未使用
            "soReturnFlag":None,
            "pageNum":1,
            "pageSize":100,
            "sourceOrderStartMonth":None,
            "sourceOrderEndMonth":None,
            "effectStartTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01',
            "effectEndTimeStr": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}'
        }
        with _mgmt_fin_voucher_second_coupon_queryList(data, access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                getSecondList = r.json()["data"]["list"][0]

    @allure.step("秒返券申请提现")
    def step_mobile_wallet_applySecondCouponWithdraw():

        data = {
            "secondCouponIdList": [getSecondList["secondCouponId"]]
        }
        with _mobile_wallet_applySecondCouponWithdraw(data, token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200

    step_mobile_personalInfo_getCurrentUserInfo()
    step_mgmt_fin_voucher_second_coupon_updateWithdrawconf()       
    step_mgmt_fin_voucher_second_coupon_queryList()
    if getSecondList:
        step_mobile_wallet_applySecondCouponWithdraw()
    
    return getSecondList

