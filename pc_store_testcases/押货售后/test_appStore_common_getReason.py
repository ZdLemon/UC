# coding:utf-8

from api.mall_store_application._appStore_common_getReason import params, _appStore_common_getReason
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/common/getReason")
class TestClass:
    """
    获取各种退换货原因
    /appStore/common/getReason
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token_85 = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("获取各种退换货原因-成功路径:押货退货时获取退货原因检查")
    def test_appStore_common_getReason(self):
        
        params = deepcopy(self.params)
        with _appStore_common_getReason(params, self.store_token_85) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



