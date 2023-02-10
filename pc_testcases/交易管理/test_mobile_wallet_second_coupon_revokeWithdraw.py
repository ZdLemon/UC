# coding:utf-8

from api.mall_mobile_application._mobile_wallet_querySecondCouponWithdrawList import _mobile_wallet_querySecondCouponWithdrawList
from api.mall_mobile_application._mobile_wallet_second_coupon_revokeWithdraw import data, _mobile_wallet_second_coupon_revokeWithdraw
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/wallet/second/coupon/revokeWithdraw")
class TestClass:
    """
    秒返券提现撤销接口
    /mobile/wallet/second/coupon/revokeWithdraw
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.severity(P1)
    @allure.title("秒返券提现撤销-成功路径: 撤销检查")
    def test_mobile_wallet_second_coupon_revokeWithdraw(self):
        
        id = None
        
        @allure.step("秒返券提现列表,获取待处理的id")
        def step_mobile_wallet_querySecondCouponWithdrawList():
            
            nonlocal id    
            with _mobile_wallet_querySecondCouponWithdrawList(access_token=self.token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        if d["withdrawStatus"] == 1:
                            id = d["id"]
                            break
                
        @allure.step("秒返券提现撤销")
        def step_mobile_wallet_second_coupon_revokeWithdraw():  
                      
            data = deepcopy(self.data)
            data["id"] = id      
            with _mobile_wallet_second_coupon_revokeWithdraw(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mobile_wallet_querySecondCouponWithdrawList()
        if id:
            step_mobile_wallet_second_coupon_revokeWithdraw()
