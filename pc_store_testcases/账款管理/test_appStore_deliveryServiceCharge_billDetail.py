# coding:utf-8

from api.mall_store_application._appStore_deliveryServiceCharge_billDetail import params, _appStore_deliveryServiceCharge_billDetail
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/deliveryServiceCharge/billDetail")
class TestClass:
    """
    配送服务费扣补明细
    /appStore/deliveryServiceCharge/billDetail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("配送服务费扣补明细-成功路径: 配送服务费扣补明细检查")
    def test_appStore_deliveryServiceCharge_billDetail(self):
        
        params = deepcopy(self.params)                 
        with _appStore_deliveryServiceCharge_billDetail(params, self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



