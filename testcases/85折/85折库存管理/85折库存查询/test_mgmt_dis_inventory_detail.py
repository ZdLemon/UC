# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_page import params, _mgmt_dis_inventory_page
from api.mall_mgmt_application._mgmt_dis_inventory_detail import params as params02, _mgmt_dis_inventory_detail

from util.getBaseMonthlyReportData import getBaseMonthlyReportData
from util.stepreruns import stepreruns
from setting import P1, P2, P3, productCode_zh, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import datetime



@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/detail")
class TestClass:
    """
    查询库存明细: 查询检查
    /mgmt/dis-inventory/detail
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询库存明细-成功路径: 默认查询当月检查")
    def test_01_mgmt_dis_inventory_detail(self):
            
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
        
        @allure.step("查询库存明细")
        def step_mgmt_dis_inventory_detail():
            
            params = deepcopy(self.params02)                 
            with _mgmt_dis_inventory_detail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["storeCode"] == inventory_page["storeCode"]
                assert r.json()["data"]["productCode"] == inventory_page["productCode"]
                assert r.json()["data"]["productName"] == inventory_page["productName"]
                assert r.json()["data"]["meterUnit"] == inventory_page["meterUnit"]
                assert r.json()["data"]["stock"] == inventory_page["stock"]
                assert r.json()["data"]["securityPrice"] == inventory_page["securityPrice"]
                assert r.json()["data"]["retailPrice"] == inventory_page["retailPrice"]
        
        step_mgmt_dis_inventory_page()
        step_mgmt_dis_inventory_detail()

    @allure.severity(P2)
    @allure.title("查询库存明细-成功路径: 查询出入库检查")
    @pytest.mark.parametrize("type,ids", [(1, "入库"), (2, "出库")])
    def test_02_mgmt_dis_inventory_detail(self, type, ids):
            
        params = deepcopy(self.params02)
        params["type"] = type        
        with _mgmt_dis_inventory_detail(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for t in set(d["type"] for d in  r.json()["data"]["page"]["list"]):
                assert t == type
            for d in r.json()["data"]["page"]["list"]:
                if type == 1:
                    assert d["bizType"] in [1, 3] # 业务类型：1押货 2押货退回 3交付 4交付退回 5库存调整
                    assert d["bizNo"].startswith("TGH") or d["bizNo"].startswith("YH") or d["bizNo"].startswith("CF") or d["bizNo"].startswith("TB")
                elif type == 2:
                    assert d["bizType"] in [2, 3, 4] # 业务类型：1押货 2押货退回 3交付 4交付退回 5库存调整
                    assert d["bizNo"].startswith("TYH") or d["bizNo"].startswith("TBB") or d["bizNo"].startswith("DTYH") or d["bizNo"].startswith("GH")
    
    @allure.severity(P2)
    @allure.title("查询库存明细-成功路径: 查询类型检查")
    @pytest.mark.parametrize("bizType,ids", [(1, "押货"), (2, "押货退货"), (3, "交付数量"), (4, "交付退回"), (5, "库存调整")])
    def test_03_mgmt_dis_inventory_detail(self, bizType, ids):
            
        params = deepcopy(self.params02)
        params["bizType"] = bizType       
        with _mgmt_dis_inventory_detail(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["page"]["list"]:
                for d in  r.json()["data"]["page"]["list"]:
                    if bizType == 1:                          # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                        assert d["bizNo"].startswith("YH") or d["bizNo"].startswith("CF") or d["bizNo"].startswith("TB")
                        assert d["bizType"] == bizType
                        assert d["diffNum"] >= 0
                        assert d["type"] == 1
                    elif bizType == 2:
                        assert d["bizNo"].startswith("DTYH") or d["bizNo"].startswith("TYH")
                        assert d["bizType"] == bizType
                        assert d["diffNum"] <= 0
                        assert d["type"] == 2
                    elif bizType == 3:
                        assert d["bizNo"].startswith("GH") or d["bizNo"].startswith("TGH")
                        assert d["bizType"] == bizType
                        assert d["type"] == 2 or 1
                        if d["type"] == 2:
                            assert d["diffNum"] <= 0
                        else:
                            assert d["diffNum"] >= 0                           
                    elif bizType == 4:
                        assert d["bizNo"].startswith("TBB")
                        assert d["bizType"] == bizType
                        assert d["diffNum"] >= 0
                        assert d["type"] == 1
                    elif bizType == 5:
                        assert d["bizType"] == bizType
                 

@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/dis-inventory/detail")
class TestClass09:
    """
    查询库存明细: 13押货转移检查
    /mgmt/dis-inventory/detail
    """
    def setup_class(self):
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("查询库存明细-成功路径: 完美运营后台-13押货转移检查")
    def test_01_mgmt_dis_inventory_detail(self, addTransfer):
            
        addTransferList, recordList = addTransfer # 库存列表:大于0的库存
        
        @allure.step("查询库存明细")
        @stepreruns()
        def step_mgmt_inventory_deposit_pageList():
                
            params = deepcopy(self.params02) 
            params["storeCode"] = store_85 
            params["productCode"] = addTransferList["serialNo"]
            with _mgmt_dis_inventory_detail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == recordList["orderSn"]
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == 1 # 交付数量
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_inventory_deposit_pageList()

    @allure.severity(P1)
    @allure.title("查询库存明细-成功路径: 店铺系统-13押货转移检查")
    def test_02_mgmt_dis_inventory_detail(self, disInventoryTransfer_addTransfer):
            
        addTransferList, recordList = disInventoryTransfer_addTransfer # 库存列表:大于0的库存
        
        @allure.step("查询库存明细")
        @stepreruns()
        def step_mgmt_inventory_deposit_pageList():
                
            params = deepcopy(self.params02) 
            params["storeCode"] = store_85 
            params["productCode"] = addTransferList["serialNo"]
            with _mgmt_dis_inventory_detail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["page"]["list"][0]["bizNo"] == recordList["orderSn"]
                assert r.json()["data"]["page"]["list"][0]["bizType"] == 1 # 业务类型：1押货 2押货退回 3交付数量 4交付退回 5库存调整
                assert time.strftime("%Y-%m-%d", time.localtime(int(r.json()["data"]["page"]["list"][0]["createTime"])/1000)) == time.strftime("%Y-%m-%d", time.localtime(time.time()))
                assert r.json()["data"]["page"]["list"][0]["diffNum"] == 1 # 交付数量
                assert r.json()["data"]["page"]["list"][0]["type"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_inventory_deposit_pageList()

