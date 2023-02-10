# coding:utf-8

from api.mall_store_application._appStore_store_getSignBankAccountList import params, _appStore_store_getSignBankAccountList
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/getSignBankAccountList")
class TestClass:
    """
    获取签约银行列表
    /appStore/store/getSignBankAccountList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("获取签约银行列表-成功路径: 获取签约银行列表检查")
    def test_appStore_store_getSignBankAccountList(self):
        
        params = deepcopy(self.params)                 
        with _appStore_store_getSignBankAccountList(params, self.store_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



