# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_settled_scope import _mgmt_dis_inventory_settled_scope

from setting import P1, P2, P3, productCode_zh, productCode, store_85, storeName_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/settled-scope")
class TestClass:
    """
    获取月结完成时间范围
    /mgmt/dis-inventory/settled-scope
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("获取月结完成时间范围-成功路径: 获取月结完成时间范围检查")
    def test_01_mgmt_dis_inventory_settled_scope(self):
            
        maxMonth = None # 最近的月结月份
        
        @allure.step("获取月结完成时间范围")
        def step_mgmt_dis_inventory_settled_scope():
            
            nonlocal maxMonth           
            with _mgmt_dis_inventory_settled_scope(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                maxMonth = r.json()["data"]["maxMonth"]
               
        step_mgmt_dis_inventory_settled_scope()









