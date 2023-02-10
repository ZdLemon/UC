# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_page import params, _mgmt_dis_inventory_page
from api.mall_mgmt_application._mgmt_dis_inventory_frozen_detail import params as params02, _mgmt_dis_inventory_frozen_detail

from setting import P1, P2, P3, productCode_zh, productCode, store_85, storeName_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/frozen-detail")
class TestClass:
    """
    查询库存冻结明细
    /mgmt/dis-inventory/frozen-detail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询库存冻结明细-成功路径: 默认查询当月检查")
    def test_01_mgmt_dis_inventory_frozen_detail(self):
            
        inventory_page = None # M7035产品库存信息
        
        @allure.step("分页查询库存列表")
        def step_mgmt_dis_inventory_page():
            
            nonlocal inventory_page
            params = deepcopy(self.params)  
            params["storeCode"] = store_85
            params["product"] = productCode              
            with _mgmt_dis_inventory_page(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                inventory_page = r.json()["data"]["list"][0]
        
        @allure.step("查询库存冻结明细")
        def step_mgmt_dis_inventory_frozen_detail():
            
            params = deepcopy(self.params02)                 
            with _mgmt_dis_inventory_frozen_detail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["storeCode"] == inventory_page["storeCode"]
                assert r.json()["data"]["storeName"] == storeName_85
                assert r.json()["data"]["productCode"] == inventory_page["productCode"]
                assert r.json()["data"]["productName"] == inventory_page["productName"]
                assert r.json()["data"]["meterUnit"] == inventory_page["meterUnit"]
                assert r.json()["data"]["stock"] == inventory_page["stock"]
                assert r.json()["data"]["securityPrice"] == inventory_page["securityPrice"]
                assert r.json()["data"]["retailPrice"] == inventory_page["retailPrice"]
                assert r.json()["data"]["frozenStock"] == inventory_page["frozenStock"]
        
        step_mgmt_dis_inventory_page()
        step_mgmt_dis_inventory_frozen_detail()

    @allure.severity(P2)
    @allure.title("查询库存冻结明细-成功路径: 查询类型检查")
    @pytest.mark.parametrize("type,ids", [(1, "冻结"), (2, "解冻")])
    def test_02_mgmt_dis_inventory_frozen_detail(self, type, ids):
            
        params = deepcopy(self.params02)
        params["type"] = type        
        with _mgmt_dis_inventory_frozen_detail(params, self.access_token) as r:
            if r.json()["data"]["page"]["list"]:
                for d in  r.json()["data"]["page"]["list"]:
                    if type == 1:
                        assert d["bizNo"].startswith("DTYH") or d["bizNo"].startswith("TYH")
                        assert d["type"] == type
                    elif type == 2:
                        assert d["bizNo"].startswith("DTYH") or d["bizNo"].startswith("TYH")
                        assert d["type"] == type
    








