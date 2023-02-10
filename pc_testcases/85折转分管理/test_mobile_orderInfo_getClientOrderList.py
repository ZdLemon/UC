# coding:utf-8

from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data, _mobile_orderInfo_getClientOrderList
from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/orderInfo/getClientOrderList")
class TestClass:
    """
    客户端订单列表查询接口
    /mobile/orderInfo/getClientOrderList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token_85 = os.environ["token_85"]

    @allure.severity(P1)
    @allure.title("客户端订单列表查询接口-成功路径: 查询85折转分订单检查")
    def test_mobile_orderInfo_getClientOrderList(self):
        
        data = deepcopy(self.data)         
        with _mobile_orderInfo_getClientOrderList(data, self.token_85) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
