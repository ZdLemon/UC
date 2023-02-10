# coding:utf-8

from api.mall_mobile_application._mobile_wallet_getSecondCouponList import data, _mobile_wallet_getSecondCouponList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/wallet/getSecondCouponList")
class TestClass:
    """
    秒返券列表
    /mobile/wallet/getSecondCouponList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["token"]

    @allure.severity(P2)
    @allure.title("秒返券列表-成功路径: 秒返券列表检查")
    def test_mobile_wallet_getSecondCouponList(self):

        data = deepcopy(self.data)
        data["couponStatusList"] = [2] # 使用状态集合，商城使用，比如：未使用传[2]；占用中传[3]；已使用传[1]；已失效传[4,5]；已提现传[6,7]
        with _mobile_wallet_getSecondCouponList(data, self.token) as r:            
            for d in r.json()["data"]["list"]:
                assert d["couponStatus"] == 2
            


