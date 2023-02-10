# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_combine import data, _mgmt_dis_inventory_combine
from api.mall_mgmt_application._mgmt_dis_inventory_combine_detail import data as data02, _mgmt_dis_inventory_combine_detail
from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/combine/detail")
class TestClass:
    """
    分页查询套装组合明细
    /mgmt/dis-inventory/combine/detail
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("分页查询套装组合明细-成功路径: 分页查询套装组合明细检查")
    def test_mgmt_dis_inventory_combine_detail(self, onSaleVersion):
        
        combineIds = None
        combine_detail = None # 组合押货单号，退货单号，押货金额，退货金额 
        
        @allure.step("套装组合: 获取combineIds")
        def step_mgmt_dis_inventory_combine():
            
            nonlocal combineIds
            data = deepcopy(self.data)
            data["productCode"] = productCode_zh
            data["storeCode"] = store_85
            data["combineNum"] = 2
            with _mgmt_dis_inventory_combine(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                combineIds = r.json()["data"]["combineId"]
        
        @allure.step("分页查询套装组合明细")
        def step_mgmt_dis_inventory_combine_detail():
            
            nonlocal combine_detail
            data = deepcopy(self.data02)
            data["combineIds"] = [str(combineIds)]
            with _mgmt_dis_inventory_combine_detail(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                combine_detail = r.json()["data"]["list"]
        
        step_mgmt_dis_inventory_combine()
        step_mgmt_dis_inventory_combine_detail()

 