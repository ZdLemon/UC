# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_disManualInputRemit_getStoreWalletMsg import params, _mgmt_inventory_disManualInputRemit_getStoreWalletMsg
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disManualInputRemit/getStoreWalletMsg")
class TestClass:
    """
    1:3押货余额及85折保证金余额查询
    /mgmt/inventory/disManualInputRemit/getStoreWalletMsg
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("1:3押货余额及85折保证金余额查询-成功路径: 手工录入流水时1:3押货余额及85折保证金余额查询检查")
    def test_mgmt_inventory_disManualInputRemit_getStoreWalletMsg(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = store_85                     
        with _mgmt_inventory_disManualInputRemit_getStoreWalletMsg(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



