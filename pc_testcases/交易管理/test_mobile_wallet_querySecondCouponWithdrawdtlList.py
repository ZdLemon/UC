# coding:utf-8

from api.mall_mobile_application._mobile_wallet_querySecondCouponWithdrawList import _mobile_wallet_querySecondCouponWithdrawList
from api.mall_mobile_application._mobile_wallet_querySecondCouponWithdrawdtlList import params, _mobile_wallet_querySecondCouponWithdrawdtlList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/wallet/querySecondCouponWithdrawdtlList")
class TestClass:
    """
    秒返券提现详情查询
    /mobile/wallet/querySecondCouponWithdrawdtlList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.token = os.environ["token"]

    @allure.severity(P1)
    @allure.title("秒返券提现详情查询-成功路径: 提现详情检查")
    def test_mobile_wallet_querySecondCouponWithdrawdtlList(self):
        
        id = None
        
        @allure.step("秒返券提现列表,获取id")
        def step_mobile_wallet_querySecondCouponWithdrawList():
            
            nonlocal id    
            with _mobile_wallet_querySecondCouponWithdrawList(access_token=self.token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]

                
        @allure.step("秒返券提现详情")
        def step_mobile_wallet_querySecondCouponWithdrawdtlList():  
                      
            params = deepcopy(self.params)
            params["withdrawId"] = id      
            with _mobile_wallet_querySecondCouponWithdrawdtlList(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mobile_wallet_querySecondCouponWithdrawList()
        step_mobile_wallet_querySecondCouponWithdrawdtlList()
