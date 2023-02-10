# coding:utf-8

from api.mall_mgmt_application._mgmt_store_listStore import params, _mgmt_store_listStore
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    获取服务中心列表
    /mgmt/store/listStore
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    
    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_01_mgmt_store_listStore(self):
        
        @allure.step("获取服务中心列表-成功路径: 精确查询存在的服务中心编号检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["storeCode"] = "902442"                
            with _mgmt_store_listStore(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert params["storeCode"] == d["code"]
        
        @allure.step("获取服务中心列表-失败路径: 模糊查询存在的服务中心编号的一部分检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["storeCode"] = "90244"                
            with _mgmt_store_listStore(params, self.access_token) as r:
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()
        

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 仅支持精确查询负责人卡号检查")
    def test_02_mgmt_store_listStore(self):
        
        @allure.step("获取服务中心列表-成功路径: 精确查询存在的负责人卡号检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderCardNo"] = "00053496"                       
            with _mgmt_store_listStore(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert d["leaderCardNo"] == "00053496"
        
        @allure.step("获取服务中心列表-失败路径: 模糊查询存在的负责人卡号的一部分检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderCardNo"] = "0005349"                       
            with _mgmt_store_listStore(params, self.access_token) as r:
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询经营地址检查")
    def test_03_mgmt_store_listStore(self):
        
        @allure.step("获取服务中心列表-成功路径: 精确查询经营地址检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["address"] = "广东省湛江市霞山区社坛路16号东新福居G幢迎福居4号商铺"                       
            with _mgmt_store_listStore(params, self.access_token) as r:           
                for d in r.json()["data"]["list"]:
                    assert params["address"] in f"{d['provinceName']}{d['cityName']}{d['areaName']}{d['detailAddress']}"
        
        @allure.step("获取服务中心列表-成功路径: 模糊查询经营地址检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["address"] = "广东省湛江市霞山区"                       
            with _mgmt_store_listStore(params, self.access_token) as r:           
                for d in r.json()["data"]["list"]:
                    assert params["address"] in f"{d['provinceName']}{d['cityName']}{d['areaName']}{d['detailAddress']}"
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 仅支持精确查询分店管理员卡号检查")
    def test_04_mgmt_store_listStore(self):
        
        @allure.step("获取服务中心列表-成功路径: 精确查询分店管理员卡号检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperNo"] = "00053496"                        
            with _mgmt_store_listStore(params, self.access_token) as r:           
                for d in r.json()["data"]["list"]:
                    assert params["shopkeeperNo"] == d["shopkeeperNo"]
        
        @allure.step("获取服务中心列表-成功路径: 模糊查询分店管理员卡号检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperNo"] = "0005349"                        
            with _mgmt_store_listStore(params, self.access_token) as r: 
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询服务中心名称检查")
    def test_mgmt_store_listStore_05(self):
        
        @allure.step("获取服务中心列表-成功路径: 精确查询服务中心名称检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["name"] = "湛江市霞山区滨海日用品专卖店"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["name"] in d["name"]
        
        @allure.step("获取服务中心列表-成功路径: 模糊查询服务中心名称检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["name"] = "湛江市霞山区滨海日用品"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["name"] in d["name"]
                            
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询负责人姓名检查")
    def test_mgmt_store_listStore_06(self):
              
        @allure.step("获取服务中心列表-成功路径: 精确负责人姓名检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderName"] = "陈海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["leaderName"] in d["leaderName"]
        
        @allure.step("获取服务中心列表-成功路径: 模糊负责人姓名检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderName"] = "海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["leaderName"] in d["leaderName"]
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询分店管理员姓名检查")
    def test_mgmt_store_listStore_07(self):
        
        @allure.step("获取服务中心列表-成功路径: 精确查询分店管理员姓名检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperName"] = "陈海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["shopkeeperName"] in d["shopkeeperName"]
        
        @allure.step("获取服务中心列表-成功路径: 模糊查询分店管理员姓名检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperName"] = "海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["shopkeeperName"] in d["shopkeeperName"]
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_mgmt_store_listStore_08(self, companyCode):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                       
        with _mgmt_store_listStore(params, self.access_token) as r:            
            for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                assert params["companyCode"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询总分店检查")
    @pytest.mark.parametrize("isMainShop", list(range(1, 3)), ids=["总店", "分店"])
    def test_mgmt_store_listStore_09(self, isMainShop):
        
        params = deepcopy(self.params)
        params["isMainShop"] = isMainShop                       
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["isMainShop"] for d in r.json()["data"]["list"]):
                assert params["isMainShop"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询网点类型检查")
    @pytest.mark.parametrize("shopType", list(range(1, 17)))
    def test_mgmt_store_listStore_10(self, shopType):
        
        params = deepcopy(self.params)
        params["shopType"] = shopType                        
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["shopType"] for d in r.json()["data"]["list"]):
                assert params["shopType"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询网点等级检查")
    @pytest.mark.parametrize("level", list(range(1, 5)))
    def test_mgmt_store_listStore_11(self, level):
        
        params = deepcopy(self.params)
        params["level"] = level                        
        with _mgmt_store_listStore(params, self.access_token) as r:            
            for i in set(d["level"] for d in r.json()["data"]["list"]):
                assert params["level"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询签署合同检查")
    @pytest.mark.parametrize("isSignContract", list(range(1, 3)), ids=["是", "否"])
    @pytest.mark.skip()
    def test_mgmt_store_listStore_12(self, isSignContract):
        
        params = deepcopy(self.params)
        params["isSignContract"] = isSignContract                       
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["isSignContract"] for d in r.json()["data"]["list"]):
                assert params["isSignContract"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询所在省份检查")
    @pytest.mark.parametrize("provinceCode", [str(i * 10000000000) for i in range(11, 66)])
    def test_mgmt_store_listStore_13(self, provinceCode):
        
        params = deepcopy(self.params)
        params["provinceCode"] = provinceCode                        
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["provinceCode"] for d in r.json()["data"]["list"]):
                assert params["provinceCode"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询经营模式检查")
    @pytest.mark.parametrize("businessMode", list(range(1, 3)), ids= ["1:3押货", "85折押货"])
    def test_mgmt_store_listStore_14(self, businessMode):
        
        params = deepcopy(self.params)
        params["businessMode"] = businessMode                        
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["businessMode"] for d in r.json()["data"]["list"]):
                assert params["businessMode"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询85折优先处理检查")
    @pytest.mark.parametrize("isHighPriority", list(range(1, 3)), ids= ["是", "否"])
    def test_mgmt_store_listStore_15(self, isHighPriority):
        
        params = deepcopy(self.params)        
        params["isHighPriority"] = isHighPriority                       
        with _mgmt_store_listStore(params, self.access_token) as r:
                        
            for i in set(d["isHighPriority"] for d in r.json()["data"]["list"]):
                assert params["isHighPriority"] == i

    @allure.story("/mgmt/store/listStore")
    @allure.severity(P2)
    @allure.title("获取服务中心列表-成功路径: 查询是否结清账务检查")
    @pytest.mark.parametrize("isSettledAccount", list(range(1, 3)), ids= ["是", "否"])
    def test_mgmt_store_listStore_16(self, isSettledAccount):
        
        params = deepcopy(self.params)
        params["isSettledAccount"] = isSettledAccount                       
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["isSettledAccount"] for d in r.json()["data"]["list"]):
                assert params["isSettledAccount"] == i


       