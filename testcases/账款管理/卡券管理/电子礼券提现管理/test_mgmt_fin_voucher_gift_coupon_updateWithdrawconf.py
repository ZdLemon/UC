# coding:utf-8

from api.mall_mgmt_application._mgmt_fin_voucher_gift_coupon_updateWithdrawconf import data, _mgmt_fin_voucher_gift_coupon_updateWithdrawconf
from setting import P1, P2, P3, username, store, username_vip

from copy import deepcopy
import os
import allure
import pytest
from itertools import combinations
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/fin/voucher/gift/coupon/updateWithdrawconf")
class TestClass:
    """
    电子礼券提现配置修改
    /mgmt/fin/voucher/gift/coupon/updateWithdrawconf
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token_2"]
        self.token = os.environ["vip_token_2"]

    @allure.severity(P2)
    @allure.title("电子礼券提现配置修改")
    def test_01_mgmt_fin_voucher_gift_coupon_updateWithdrawconf(self):
        
        @allure.step("电子礼券提现配置修改")
        def step_mgmt_fin_voucher_gift_coupon_updateWithdrawconf():
            
            data = deepcopy(self.data)       
            with _mgmt_fin_voucher_gift_coupon_updateWithdrawconf(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_fin_voucher_gift_coupon_updateWithdrawconf()

    @allure.severity(P2)
    @allure.title("电子礼券提现配置修改-失败路径：电子礼券提现金额小于配置，不允许提现")
    def test_02_mgmt_fin_voucher_gift_coupon_updateWithdrawconf(self):
        
        from api.mall_mobile_application._mobile_wallet_getGiftCouponByMemberIdAndStatus import data as data01, _mobile_wallet_getGiftCouponByMemberIdAndStatus # 查询电子礼券发放信息
        from api.mall_mobile_application._mobile_web_wallet_queryGiftCouponAmt import _mobile_web_wallet_queryGiftCouponAmt # 可用电子礼券金额统计
        from api.mall_mobile_application._mobile_wallet_gift_coupon_queryWithdrawconf import _mobile_wallet_gift_coupon_queryWithdrawconf # 电子礼券提现配置查询
        from api.mall_mobile_application._mobile_wallet_queryGiftCouponSurveyByMemberId import _mobile_wallet_queryGiftCouponSurveyByMemberId # 电子礼券调查配置项显示
        from api.mall_mobile_application._mobile_wallet_checkGiftCouponWithdraw import _mobile_wallet_checkGiftCouponWithdraw # 电子礼券提现校验
        from api.mall_mobile_application._mobile_wallet_applyGiftCouponWithdraw import _mobile_wallet_applyGiftCouponWithdraw # 电子礼券申请提现
        
        queryWithdrawconf = None # 电子礼券提现配置查询
        giftCouponIdList = [] # 电子礼券id集合
        giftCouponCardAmount = 0 # 电子礼券集合金额
        giftCouponCode = [] # 电子礼券code集合
        
        @allure.step("电子礼券提现配置修改")
        def step_mgmt_fin_voucher_gift_coupon_updateWithdrawconf():
            
            deepcopy(self.data)
            data["minAmount"] = 1000 # 单次提现合计金额下限
            with _mgmt_fin_voucher_gift_coupon_updateWithdrawconf(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("查询电子礼券发放信息")
        def step_mobile_wallet_getGiftCouponByMemberIdAndStatus():
            
            nonlocal giftCouponIdList, giftCouponCardAmount, giftCouponCode
            
            data = deepcopy(data01)
            data["giftCouponStatus"] = 2 # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 6:已失效 不传或者null:全部     
            with _mobile_wallet_getGiftCouponByMemberIdAndStatus(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200 
                if r.json()["data"]["list"]:
                    giftCouponIdList.append(r.json()["data"]["list"][i]["grantdtlId"])
                    giftCouponCardAmount += r.json()["data"]["list"][i]["giftCouponCardAmount"]
                    giftCouponCode.append(r.json()["data"]["list"][i]["giftCouponCode"])
        
        @allure.step("可用电子礼券金额统计")
        def step_mobile_web_wallet_queryGiftCouponAmt():
                
            with _mobile_web_wallet_queryGiftCouponAmt(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200 
        
        @allure.step("电子礼券提现配置查询")
        def step_mobile_wallet_gift_coupon_queryWithdrawconf():
            
            nonlocal queryWithdrawconf
                
            with _mobile_wallet_gift_coupon_queryWithdrawconf(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["minAmount"] > giftCouponCardAmount 
                queryWithdrawconf = r.json()["data"]["minAmount"]
        
        @allure.step("电子礼券调查配置项显示")
        def step_mobile_wallet_queryGiftCouponSurveyByMemberId():
                
            with _mobile_wallet_queryGiftCouponSurveyByMemberId(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200 

        @allure.step("电子礼券提现校验")
        def step_mobile_wallet_checkGiftCouponWithdraw():
                
            with _mobile_wallet_checkGiftCouponWithdraw(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200 

        @allure.step("电子礼券申请提现")
        def step_mobile_wallet_applyGiftCouponWithdraw():
            
            data = {
                "giftCouponIdList": giftCouponIdList # 电子礼券id集合
            }    
            with _mobile_wallet_applyGiftCouponWithdraw(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 500
                assert r.json()["message"] == f"需满{int(queryWithdrawconf)}.00元才可提现"
        
        step_mgmt_fin_voucher_gift_coupon_updateWithdrawconf()
        for i in range(1):
            step_mobile_wallet_getGiftCouponByMemberIdAndStatus()
        if giftCouponIdList:
            step_mobile_web_wallet_queryGiftCouponAmt()
            step_mobile_wallet_gift_coupon_queryWithdrawconf()
            step_mobile_wallet_queryGiftCouponSurveyByMemberId()
            step_mobile_wallet_checkGiftCouponWithdraw()
            step_mobile_wallet_applyGiftCouponWithdraw()
    
            

    