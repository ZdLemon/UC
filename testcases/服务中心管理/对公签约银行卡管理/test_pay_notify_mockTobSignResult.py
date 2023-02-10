# coding:utf-8

from api.mall_center_pay._pay_notify_mockTobSignResult import data, _pay_notify_mockTobSignResult
from setting import P1, P2, P3, username_vip

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/pay/notify/mockTobSignResult")
@pytest.mark.skip()
class TestClass:
    """
    模拟发送工行企业代扣签约
    /pay/notify/mockTobSignResult
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("模拟发送工行企业代扣签约")
    def test_pay_notify_mockTobSignResult(self):
            
        data = deepcopy(self.data)  
        data["accName"] = "东河区聚呈信息服务部"
        data["accNo"] = "0603032009224800453"           
        with _pay_notify_mockTobSignResult(data, self.access_token) as r:
            assert r.status_code == 200
        


        


 