# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_remit_getSourceTypeByRemitType import params, _mgmt_inventory_remit_getSourceTypeByRemitType
from setting import P1, P2, P3, username, mobile, username_vip, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/remit/getSourceTypeByRemitType")
class TestClass:
    """
    按银行流水类型获取款项映射列表
    /mgmt/inventory/remit/getSourceTypeByRemitType
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("按银行流水类型获取款项映射列表: 手工录入流水时检查")
    def test_mgmt_inventory_remit_getSourceTypeByRemitType(self):
        
        getSourceTypeByRemitType = "" # 按银行流水类型获取款项映射列表
        
        @allure.step("按银行流水类型获取款项映射列表")
        def step_mgmt_inventory_remit_getSourceTypeByRemitType():
            
            nonlocal getSourceTypeByRemitType
            params = deepcopy(self.params)               
            with _mgmt_inventory_remit_getSourceTypeByRemitType(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getSourceTypeByRemitType = r.json()["data"]
        
        step_mgmt_inventory_remit_getSourceTypeByRemitType()

        

