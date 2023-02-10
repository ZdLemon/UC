# coding:utf-8

from api.basic_services._login import _login
from api.mall_mgmt_application._mgmt_inventory_remit_unknownRemit_pageList import data, _mgmt_inventory_remit_unknownRemit_pageList
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/remit/unknownRemit/pageList")
class TestClass:
    """
    未知款项流水分页搜索列表
    /mgmt/inventory/remit/unknownRemit/pageList
    """
    
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P2)
    @allure.title("未知款项流水分页搜索列表-成功路径：仅支持精确查询服务中心编号检查") 
    @pytest.mark.parametrize("storeCode", [store_85, store_85[:-1]], ids=["完整的服务中心编号", "服务中心编号的一部分"])
    def test_01_mgmt_inventory_remit_unknownRemit_pageList(self, storeCode):
        
        data = deepcopy(self.data)
        data["storeCode"] = storeCode
        with _mgmt_inventory_remit_unknownRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["storeCode"] == storeCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("未知款项流水分页搜索列表-成功路径：查询分公司编号检查") 
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_02_mgmt_inventory_remit_unknownRemit_pageList(self, companyCode):
        
        data = deepcopy(self.data)
        data["companyCode"] = companyCode
        with _mgmt_inventory_remit_unknownRemit_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []



