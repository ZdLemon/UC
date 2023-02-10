# coding:utf-8

from api.mall_mgmt_application._mgmt_store_getStoreLevelList import params, _mgmt_store_getStoreLevelList
from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/getStoreLevelList")
class TestClass:
    """
    查询网点等级列表
    /mgmt/store/getStoreLevelList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_01_mgmt_store_getStoreLevelList(self):
        
        getStoreLevelList = None
        
        @allure.step("查询网点等级列表")
        def step_01_mgmt_store_getStoreLevelList():
            
            nonlocal getStoreLevelList
            params = deepcopy(self.params)               
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreLevelList = r.json()["data"]["list"][0]
        
        @allure.step("查询网点等级列表-成功路径: 精确查询服务中心编号检查")
        def step_02_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["storeCode"] = getStoreLevelList["storeCode"]              
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["storeCode"] == getStoreLevelList["storeCode"]
        
        step_01_mgmt_store_getStoreLevelList()
        step_02_mgmt_store_getStoreLevelList()
        
    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询服务中心星级单选检查")
    @pytest.mark.parametrize("level", [1, 2, 3, 4])
    def test_02_mgmt_store_getStoreLevelList(self, level):
        
        @allure.step("查询网点等级列表")
        def step_01_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["level"] = level # 网点等级 1服务中心 2五星服务中心 3五星旗舰服务中心 4无实体店，多个用逗号分隔                      
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["level"] == level
        
        step_01_mgmt_store_getStoreLevelList()

    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询服务中心星级多选检查")
    def test_021_mgmt_store_getStoreLevelList(self):
        
        @allure.step("查询网点等级列表")
        def step_01_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["level"] = 1,2 # 网点等级 1服务中心 2五星服务中心 3五星旗舰服务中心 4无实体店，多个用逗号分隔                      
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["level"] == 1 or d["level"] == 2

        @allure.step("查询网点等级列表")
        def step_02_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["level"] = "3,4" # 网点等级 1服务中心 2五星服务中心 3五星旗舰服务中心 4无实体店，多个用逗号分隔                      
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["level"] == 3 or d["level"] == 4
                        
        @allure.step("查询网点等级列表")
        def step_03_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["level"] = "1,2,3,4" # 网点等级 1服务中心 2五星服务中心 3五星旗舰服务中心 4无实体店，多个用逗号分隔                      
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for d in r.json()["data"]["list"]:
                        assert d["level"] == 1 or d["level"] == 2 or d["level"] == 3 or d["level"] == 4
                                                        
        step_01_mgmt_store_getStoreLevelList()
        step_02_mgmt_store_getStoreLevelList()
        step_03_mgmt_store_getStoreLevelList()

    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_03_mgmt_store_getStoreLevelList(self, companyCode):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                       
        with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:          
                for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                    assert params["companyCode"] == i

    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 仅支持精确查询负责人卡号检查")
    def test_04_mgmt_store_getStoreLevelList(self):
        
        getStoreLevelList = None
        
        @allure.step("查询网点等级列表")
        def step_01_mgmt_store_getStoreLevelList():
            
            nonlocal getStoreLevelList
            params = deepcopy(self.params)               
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreLevelList = r.json()["data"]["list"][0]
        
        @allure.step("查询网点等级列表-成功路径: 精确查询负责人卡号检查")
        def step_02_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["leaderNo"] = getStoreLevelList["leaderNo"]              
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["leaderNo"] == getStoreLevelList["leaderNo"]
        
        step_01_mgmt_store_getStoreLevelList()
        step_02_mgmt_store_getStoreLevelList()
       
    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询网点类型检查")
    @pytest.mark.parametrize("shopType", [i for i in range(1, 17)])
    def test_05_mgmt_store_getStoreLevelList(self, shopType):
        
        params = deepcopy(self.params)
        params["shopType"] = shopType                       
        with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:          
                for i in set(d["shopType"] for d in r.json()["data"]["list"]):
                    assert i == shopType

    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询省份检查")
    def test_06_mgmt_store_getStoreLevelList(self):
        
        params = deepcopy(self.params)
        getProvinceList = []
        
        @allure.step("查询网点等级列表")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList              
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProvinceList = r.json()["data"]
        
        @allure.step("查询网点等级列表")
        def step_mgmt_store_getStoreLevelList():
            
            params["provinceCode"] = getProvince["provinceCode"]            
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:  
                    for i in set(d["provinceName"] for d in r.json()["data"]["list"]):
                        assert i == getProvince["provinceName"]                                 
        
        step_mgmt_sys_getProvinceList()
        for getProvince in getProvinceList:
            step_mgmt_store_getStoreLevelList()
       
    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询年份检查")
    def test_07_mgmt_store_getStoreLevelList(self):
        
        getStoreLevelList = None
        
        @allure.step("查询网点等级列表")
        def step_01_mgmt_store_getStoreLevelList():
            
            nonlocal getStoreLevelList
            params = deepcopy(self.params)               
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    getStoreLevelList = r.json()["data"]["list"][0]
        
        @allure.step("查询网点等级列表")
        def step_02_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["year"] = getStoreLevelList["year"]              
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:  
                    for i in set(d["year"] for d in r.json()["data"]["list"]):
                        assert i == getStoreLevelList["year"] 
        
        step_01_mgmt_store_getStoreLevelList()
        step_02_mgmt_store_getStoreLevelList()
       
    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询取消类型检查")
    @pytest.mark.parametrize("cancelType", [i for i in range(1, 7)])
    def test_08_mgmt_store_getStoreLevelList(self, cancelType):
        
        @allure.step("查询网点等级列表")
        def step_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["cancelType"] = cancelType # 取消类型: 1、结点取消，2、转让取消，3、违规取消，4、不达标取消，5、冻结取消，6、转云取消             
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:  
                    for i in set(d["cancelType"] for d in r.json()["data"]["list"]):
                        assert i == cancelType
        
        step_mgmt_store_getStoreLevelList()
       
    @allure.severity(P2)
    @allure.title("查询网点等级列表-成功路径: 查询是否取消检查")
    @pytest.mark.parametrize("isCancel", [1, 0])
    def test_09_mgmt_store_getStoreLevelList(self, isCancel):
        
        @allure.step("查询网点等级列表")
        def step_mgmt_store_getStoreLevelList():
            
            params = deepcopy(self.params)
            params["isCancel"] = isCancel # 是否取消: 1、是，0、否           
            with _mgmt_store_getStoreLevelList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:  
                    for i in set(d["isCancel"] for d in r.json()["data"]["list"]):
                        assert i == isCancel
        
        step_mgmt_store_getStoreLevelList()
       









