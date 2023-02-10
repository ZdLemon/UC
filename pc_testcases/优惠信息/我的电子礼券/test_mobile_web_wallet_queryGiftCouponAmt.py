# coding:utf-8

from api.mall_mobile_application._mobile_wallet_getGiftCouponByMemberIdAndStatus import data, _mobile_wallet_getGiftCouponByMemberIdAndStatus # 查询电子礼券发放信息
from api.mall_mobile_application._mobile_web_wallet_queryGiftCouponAmt import _mobile_web_wallet_queryGiftCouponAmt # 可用电子礼券金额统计

from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall-mobile-application")
@allure.story("/mobile/web/wallet/queryGiftCouponAmt")
class TestClass:
    """
    可用电子礼券金额统计
    /mobile/web/wallet/queryGiftCouponAmt
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.data = deepcopy(data)

    @allure.severity(P2)
    @allure.title("可用电子礼券金额统计: 可用电子礼券金额统计检查")
    def test_mobile_web_wallet_queryGiftCouponAmt(self):
        
        getGiftCouponByMemberIdAndStatus = None # 电子礼券信息
        
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
   
        step_mobile_wallet_getGiftCouponByMemberIdAndStatus()
        step_mobile_web_wallet_queryGiftCouponAmt()