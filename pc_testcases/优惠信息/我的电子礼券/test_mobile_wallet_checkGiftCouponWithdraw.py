# coding:utf-8

from api.mall_mobile_application._mobile_wallet_getGiftCouponByMemberIdAndStatus import data, _mobile_wallet_getGiftCouponByMemberIdAndStatus # 查询电子礼券发放信息
from api.mall_mobile_application._mobile_web_wallet_queryGiftCouponAmt import _mobile_web_wallet_queryGiftCouponAmt # 可用电子礼券金额统计
from api.mall_mobile_application._mobile_wallet_gift_coupon_queryWithdrawconf import _mobile_wallet_gift_coupon_queryWithdrawconf # 电子礼券提现配置查询
from api.mall_mobile_application._mobile_wallet_queryGiftCouponSurveyByMemberId import _mobile_wallet_queryGiftCouponSurveyByMemberId # 电子礼券调查配置项显示
from api.mall_mobile_application._mobile_wallet_checkGiftCouponWithdraw import _mobile_wallet_checkGiftCouponWithdraw # 电子礼券提现校验

from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall-mobile-application")
@allure.story("/mobile/wallet/checkGiftCouponWithdraw")
class TestClass:
    """
    电子礼券提现校验
    /mobile/wallet/checkGiftCouponWithdraw
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.data = deepcopy(data)

    @allure.severity(P2)
    @allure.title("电子礼券提现校验: 电子礼券提现校验")
    def test_mobile_wallet_checkGiftCouponWithdraw(self):
        
        getGiftCouponByMemberIdAndStatus = None # 电子礼券信息
        queryWithdrawconf = None # 电子礼券提现配置查询
        
        @allure.step("查询电子礼券发放信息")
        def step_mobile_wallet_getGiftCouponByMemberIdAndStatus():
            
            nonlocal getGiftCouponByMemberIdAndStatus
            
            data = deepcopy(self.data)
            data["giftCouponStatus"] = 2 # 状态 1:已使用 2:未使用 3:占用中 4:冻结中 5:已转出 6:已失效 不传或者null:全部     
            with _mobile_wallet_getGiftCouponByMemberIdAndStatus(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200 
                getGiftCouponByMemberIdAndStatus = r.json()["data"]["list"][0]
        
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
   
        step_mobile_wallet_getGiftCouponByMemberIdAndStatus()
        step_mobile_web_wallet_queryGiftCouponAmt()
        step_mobile_wallet_gift_coupon_queryWithdrawconf()
        step_mobile_wallet_queryGiftCouponSurveyByMemberId()
        step_mobile_wallet_checkGiftCouponWithdraw()