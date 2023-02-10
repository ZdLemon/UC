# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_disInventoryTransfer_pageList import data, _mgmt_inventory_disInventoryTransfer_pageList


from setting import P1, P2, P3, productCode_zh, productCode, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/disInventoryTransfer/pageList")
class TestClass:
    """
    押货转移管理列表
    /mgmt/inventory/disInventoryTransfer/pageList
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P3)
    @allure.title("押货转移管理列表-成功路径: 查询默认条件检查")
    def test_00_mgmt_inventory_disInventoryTransfer_pageList(self):
            
        data = deepcopy(self.data)                 
        with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("押货转移管理列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_01_mgmt_inventory_disInventoryTransfer_pageList(self):
        
        storeCode = None
            
        @allure.step("获取服务中心编号")
        def step_01_mgmt_inventory_disInventoryTransfer_pageList():
            
            nonlocal storeCode
            data = deepcopy(self.data) 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                storeCode = r.json()["data"]["list"][0]["storeCode"]

        @allure.step("精确查询服务中心编号")
        def step_02_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = storeCode 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeCode"] == storeCode

        @allure.step("不支持模糊查询服务中心编号")
        def step_03_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["storeCode"] = storeCode[:-1] 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_disInventoryTransfer_pageList()
        step_02_mgmt_inventory_disInventoryTransfer_pageList()
        step_03_mgmt_inventory_disInventoryTransfer_pageList()

    @allure.severity(P3)
    @allure.title("押货转移管理列表-成功路径: 支持模糊查询服务中心名称检查")
    def test_02_mgmt_inventory_disInventoryTransfer_pageList(self):
        
        storeName = None
            
        @allure.step("获取服务中心名称")
        def step_01_mgmt_inventory_disInventoryTransfer_pageList():
            
            nonlocal storeName
            data = deepcopy(self.data) 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                storeName = r.json()["data"]["list"][0]["storeName"]

        @allure.step("精确查询服务中心名称")
        def step_02_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["storeName"] = storeName 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert storeName in i["storeName"]

        @allure.step("支持模糊查询服务中心名称")
        def step_03_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["storeName"] = storeName[:-1] 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert storeName[:-1] in i["storeName"]
        
        step_01_mgmt_inventory_disInventoryTransfer_pageList()
        step_02_mgmt_inventory_disInventoryTransfer_pageList()
        step_03_mgmt_inventory_disInventoryTransfer_pageList()

    @allure.severity(P2)
    @allure.title("押货转移管理列表-成功路径: 仅支持精确查询负责人卡号检查")
    def test_03_mgmt_inventory_disInventoryTransfer_pageList(self):
        
        leaderNo = None
            
        @allure.step("获取负责人卡号")
        def step_01_mgmt_inventory_disInventoryTransfer_pageList():
            
            nonlocal leaderNo
            data = deepcopy(self.data) 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                leaderNo = r.json()["data"]["list"][0]["leaderNo"]

        @allure.step("精确查询负责人卡号")
        def step_02_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["leaderNo"] = leaderNo 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["leaderNo"] == leaderNo

        @allure.step("不支持模糊查询负责人卡号")
        def step_03_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["leaderNo"] = leaderNo[:-1] 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_disInventoryTransfer_pageList()
        step_02_mgmt_inventory_disInventoryTransfer_pageList()
        step_03_mgmt_inventory_disInventoryTransfer_pageList()

    @allure.severity(P3)
    @allure.title("押货转移管理列表-成功路径: 支持模糊查询负责人名称检查")
    def test_04_mgmt_inventory_disInventoryTransfer_pageList(self):
        
        leaderName = None
            
        @allure.step("获取负责人名称")
        def step_01_mgmt_inventory_disInventoryTransfer_pageList():
            
            nonlocal leaderName
            data = deepcopy(self.data) 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                leaderName = r.json()["data"]["list"][0]["leaderName"]

        @allure.step("精确查询负责人名称")
        def step_02_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["leaderName"] = leaderName 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert leaderName in i["leaderName"]

        @allure.step("支持模糊查询负责人名称")
        def step_03_mgmt_inventory_disInventoryTransfer_pageList():
            
            data = deepcopy(self.data)
            data["leaderName"] = leaderName[:-1] 
            data["changeStartDate"] = ""
            data["changeEndDate"] = ""                 
            with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    assert leaderName[:-1] in i["leaderName"]
        
        step_01_mgmt_inventory_disInventoryTransfer_pageList()
        step_02_mgmt_inventory_disInventoryTransfer_pageList()
        step_03_mgmt_inventory_disInventoryTransfer_pageList()

    @allure.severity(P3)
    @allure.title("押货转移管理列表-成功路径: 查询网点类型检查")
    @pytest.mark.parametrize("shopType", [i for i in range(1, 17)])
    def test_05_mgmt_inventory_disInventoryTransfer_pageList(self, shopType):
            
        data = deepcopy(self.data) 
        data["shopType"] = shopType 
        data["changeStartDate"] = ""
        data["changeEndDate"] = ""                 
        with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["shopType"] for d in r.json()["data"]["list"]):
                    assert i == shopType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P3)
    @allure.title("押货转移管理列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_06_mgmt_inventory_disInventoryTransfer_pageList(self, companyCode):
            
        data = deepcopy(self.data) 
        data["companyCode"] = [str(companyCode)]
        data["changeStartDate"] = ""
        data["changeEndDate"] = ""                   
        with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert i == companyCode
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("押货转移管理列表-成功路径: 查询账务是否结清检查")
    @pytest.mark.parametrize("settleAccount,ids", [(0, "未结清"), (1, "已结清"), ])
    def test_07_mgmt_inventory_disInventoryTransfer_pageList(self, settleAccount, ids):
            
        data = deepcopy(self.data)
        data["settleAccount"] = settleAccount # 结清账户 0未结清 1已结清
        data["changeStartDate"] = ""
        data["changeEndDate"] = ""   
        with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert d["settleAccount"] == settleAccount
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("押货转移管理列表-成功路径: 查询库存是否为0检查")
    @pytest.mark.parametrize("inventoryIsZero,ids", [(0, "为0"), (1, "不为0"), ])
    def test_08_mgmt_inventory_disInventoryTransfer_pageList(self, inventoryIsZero, ids):
            
        data = deepcopy(self.data)
        data["inventoryIsZero"] = inventoryIsZero # 库存是否为0: 0为0 1不为0
        data["changeStartDate"] = ""
        data["changeEndDate"] = ""   
        with _mgmt_inventory_disInventoryTransfer_pageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                if inventoryIsZero == 0:
                    for d in r.json()["data"]["list"]:
                        assert d["mortgageInventoryTotal"] == 0
                else:
                    for d in r.json()["data"]["list"]:
                        assert d["mortgageInventoryTotal"] != 0
            else:
                assert r.json()["data"]["list"] == []

