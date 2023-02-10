# coding:utf-8

from api.mall_mgmt_application._mgmt_store_listStore import _mgmt_store_listStore
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/listStore")
class TestClass:
    """
    获取服务中心权限配置列表(服务中心权限配置)
    /mgmt/store/listStore
    """
    def setup_class(self):
        self.params = {
            "storeCode" : "",  # str服务中心编号
            "name" : "",   # str服务中心名称
            "leaderCardNo": "", # str总店负责人卡号
            "leaderName" : "",  # str负责人姓名
            "shopType" : None,  # int网点类型1、微店 2、微店(账务未清)3、微店(办理结店中)4、微店(结店)5、冻结资格6、办理结点中7、取消（账务未结清）8、新批未运作9、正式网点10、结店（保店二年1、结店12、结店（保店一年13、结店（保店三年）
            "shopkeeperName" : "",  # 分店管理员姓名
            "shopkeeperNo" : "",  # 分店管理员卡号
            "isMainShop" : None,  # int是否总店 0总店 1分店
            "provinceCode" : "",  # str省份code
            "pageNum": 1,  # int页码
            "pageSize": 20,  # int页数量
        }
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("获取服务中心权限配置列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_01_mgmt_store_listStore(self):
        
        @allure.step("获取服务中心权限配置列表-成功路径: 精确查询存在的服务中心编号检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["storeCode"] = "902442"                
            with _mgmt_store_listStore(params, self.access_token) as r:
                assert r.json()["data"]["list"][0]["code"] == params["storeCode"]
        
        @allure.step("获取服务中心权限配置列表-失败路径: 模糊查询存在的服务中心编号的一部分检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["storeCode"] = "90244"                
            with _mgmt_store_listStore(params, self.access_token) as r:
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()
        
    @allure.severity(P2)
    @allure.title("获取服务中心权限配置列表-成功路径: 仅支持精确查询负责人卡号检查")
    def test_02_mgmt_store_listStore(self):
        
        @allure.step("获取服务中心权限配置列表-成功路径: 精确查询存在的负责人卡号检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderCardNo"] = "00053496"                       
            with _mgmt_store_listStore(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    assert d["leaderCardNo"] == "00053496"
        
        @allure.step("获取服务中心权限配置列表-失败路径: 模糊查询存在的负责人卡号的一部分检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderCardNo"] = "0005349"                       
            with _mgmt_store_listStore(params, self.access_token) as r:
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.severity(P3)
    @allure.title("获取服务中心权限配置列表-成功路径: 仅支持精确查询分店管理员卡号检查")
    def test_04_mgmt_store_listStore(self):
        
        @allure.step("获取服务中心权限配置列表-成功路径: 精确查询分店管理员卡号检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperNo"] = "00053496"                        
            with _mgmt_store_listStore(params, self.access_token) as r:           
                for d in r.json()["data"]["list"]:
                    assert params["shopkeeperNo"] == d["shopkeeperNo"]
        
        @allure.step("获取服务中心权限配置列表-成功路径: 模糊查询分店管理员卡号检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperNo"] = "0005349"                        
            with _mgmt_store_listStore(params, self.access_token) as r: 
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.severity(P2)
    @allure.title("获取服务中心权限配置列表-成功路径: 查询服务中心名称检查")
    def test_04_mgmt_store_listStore_05(self):
        
        @allure.step("获取服务中心权限配置列表-成功路径: 精确查询服务中心名称检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["name"] = "湛江市霞山区滨海日用品专卖店"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["name"] in d["name"]
        
        @allure.step("获取服务中心权限配置列表-成功路径: 模糊查询服务中心名称检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["name"] = "湛江市霞山区滨海日用品"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["name"] in d["name"]
                            
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.severity(P3)
    @allure.title("获取服务中心权限配置列表-成功路径: 查询负责人姓名检查")
    def test_05_mgmt_store_listStore_06(self):
              
        @allure.step("获取服务中心权限配置列表-成功路径: 精确负责人姓名检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderName"] = "陈海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["leaderName"] in d["leaderName"]
        
        @allure.step("获取服务中心权限配置列表-成功路径: 模糊负责人姓名检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["leaderName"] = "海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["leaderName"] in d["leaderName"]
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.severity(P3)
    @allure.title("获取服务中心权限配置列表-成功路径: 查询分店管理员姓名检查")
    def test_06_mgmt_store_listStore_07(self):
        
        @allure.step("获取服务中心权限配置列表-成功路径: 精确查询分店管理员姓名检查")
        def step_01_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperName"] = "陈海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["shopkeeperName"] in d["shopkeeperName"]
        
        @allure.step("获取服务中心权限配置列表-成功路径: 模糊查询分店管理员姓名检查")
        def step_02_mgmt_store_listStore():
            params = deepcopy(self.params)
            params["shopkeeperName"] = "海雯"                        
            with _mgmt_store_listStore(params, self.access_token) as r:            
                for d in r.json()["data"]["list"]:
                    assert params["shopkeeperName"] in d["shopkeeperName"]
        
        step_01_mgmt_store_listStore()
        step_02_mgmt_store_listStore()

    @allure.severity(P3)
    @allure.title("获取服务中心权限配置列表-成功路径: 查询分公司检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_07_mgmt_store_listStore_08(self, companyCode):
        
        params = deepcopy(self.params)
        params["companyCode"] = companyCode                       
        with _mgmt_store_listStore(params, self.access_token) as r:            
            for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                assert params["companyCode"] == i

    @allure.severity(P3)
    @allure.title("获取服务中心权限配置列表-成功路径: 查询总分店检查")
    @pytest.mark.parametrize("isMainShop", list(range(1, 3)), ids=["总店", "分店"])
    def test_08_mgmt_store_listStore_09(self, isMainShop):
        
        params = deepcopy(self.params)
        params["isMainShop"] = isMainShop                       
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["isMainShop"] for d in r.json()["data"]["list"]):
                assert params["isMainShop"] == i

    @allure.severity(P3)
    @allure.title("获取服务中心权限配置列表-成功路径: 查询网点类型检查")
    @pytest.mark.parametrize("shopType", list(range(1, 17)))
    def test_09_mgmt_store_listStore_10(self, shopType):
        
        params = deepcopy(self.params)
        params["shopType"] = shopType                        
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["shopType"] for d in r.json()["data"]["list"]):
                assert params["shopType"] == i

    @allure.severity(P3)
    @allure.title("获取服务中心权限配置列表-成功路径: 查询所在省份检查")
    @pytest.mark.parametrize("provinceCode", [str(i * 10000000000) for i in range(11, 66)])
    def test_10_mgmt_store_listStore_13(self, provinceCode):
        
        params = deepcopy(self.params)
        params["provinceCode"] = provinceCode                        
        with _mgmt_store_listStore(params, self.access_token) as r:           
            for i in set(d["provinceCode"] for d in r.json()["data"]["list"]):
                assert params["provinceCode"] == i


       