# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_split import data, _mgmt_dis_inventory_split
from api.mall_mgmt_application._mgmt_dis_inventory_split_record_page import data as data02, _mgmt_dis_inventory_split_record_page
from api.mall_mgmt_application._mgmt_dis_inventory_split_detail import data as data03, _mgmt_dis_inventory_split_detail
from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/split")
class TestClass:
    """
    套装拆分
    /mgmt/dis-inventory/split
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("套装拆分-成功路径: 套装拆分检查")
    def test_mgmt_dis_inventory_split(self):
        
        id = None
        split_detail = None
        
        @allure.step("套装拆分")
        def test_mgmt_dis_inventory_split():
            
            data = deepcopy(self.data)
            data["productCodes"] = [productCode_zh]
            with _mgmt_dis_inventory_split(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                
        @allure.step("查询套装拆分列表:获取id")
        def step_mgmt_dis_inventory_split_record_page():
            
            nonlocal id
            data = deepcopy(data02)
            data["product"] = productCode_zh
            with _mgmt_dis_inventory_split_record_page(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("套装拆明细")
        def step_mgmt_dis_inventory_split_detail():
            
            nonlocal split_detail
            data = deepcopy(data03)
            data["id"] = id
            with _mgmt_dis_inventory_split_detail(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                split_detail = r.json()["data"]["list"]
        
        test_mgmt_dis_inventory_split()
        step_mgmt_dis_inventory_split_record_page()
        step_mgmt_dis_inventory_split_detail()

    
