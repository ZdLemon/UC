# coding:utf-8

from api.mall_store_application._appStore_store_deposit_msg import params, _appStore_store_deposit_msg
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/deposit/msg")
class TestClass:
    """
    获取服务中心可用押货保证金余额
    /appStore/store/deposit/msg
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("获取服务中心可用押货保证金余额-成功路径:押货时获取服务中心可用押货保证金余额检查")
    def test_appStore_store_deposit_msg(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = store_85
        with _appStore_store_deposit_msg(params, self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["balance"] > 0



