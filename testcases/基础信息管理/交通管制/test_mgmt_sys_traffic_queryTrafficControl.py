# coding:utf-8

from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息
from api.mall_center_sys._mgmt_sys_getCityList import _mgmt_sys_getCityList # 根据省份编码获取下属城市
from api.mall_center_sys._mgmt_sys_getRegionListByCity import _mgmt_sys_getRegionListByCity # 根据城市编码获取下属地区
from api.mall_center_sys._mgmt_sys_getStreetListByDistrictCode import _mgmt_sys_getStreetListByDistrictCode # 根据地区编码获取下属街道

from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/traffic/queryTrafficControl")
class TestClass:
    """
    分页查询交通管制
    /mgmt/sys/traffic/queryTrafficControl
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("分页查询交通管制-成功路径: 查询省份检查")
    def test_01_mgmt_sys_traffic_queryTrafficControl(self):
        
        getProvinceLists = [] # 省份编码
        
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceLists                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getProvinceLists.append(d["code"])   

        @allure.step("分页查询交通管制：查询省份")
        def step_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)   
            data["provinceCode"] = provinceCode                  
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["provinceCode"] for d in r.json()["data"]["list"]):
                    assert i == provinceCode
        
        step_mgmt_sys_getProvinceList()
        for provinceCode in getProvinceLists:
            step_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("分页查询交通管制-成功路径: 查询城市检查")
    def test_02_mgmt_sys_traffic_queryTrafficControl(self):
        
        getProvinceLists = [] # 省份编码
        getCityLists = [] # 城市编码
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceLists                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getProvinceLists.append(d["code"])   

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": provinceCode, # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getCityLists.append(d["code"])  

        @allure.step("分页查询交通管制：查询城市")
        def step_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)   
            data["provinceCode"] = provinceCode 
            data["cityCode"] = cityCode                
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["cityCode"] for d in r.json()["data"]["list"]):
                        assert i == cityCode
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getProvinceList()
        for provinceCode in getProvinceLists[0]:
            step_mgmt_sys_getCityList()
            for cityCode in getCityLists[0]:
                step_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("分页查询交通管制-成功路径: 查询地区检查")
    def test_03_mgmt_sys_traffic_queryTrafficControl(self):
        
        getProvinceLists = [] # 省份编码
        getCityLists = [] # 城市编码
        getRegionListByCitys = [] # 地区编码
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceLists                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getProvinceLists.append(d["code"])   

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": provinceCode, # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getCityLists.append(d["code"])  

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getRegionListByCity():
            
            nonlocal getRegionListByCitys
            params = {
                "cityCode": cityCode  # str城市编码
            }                   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getRegionListByCitys.append(d["code"])  

        @allure.step("分页查询交通管制：查询地区")
        def step_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)   
            data["provinceCode"] = provinceCode 
            data["cityCode"] = cityCode
            data["districtCode"] = districtCode              
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["districtCode"] for d in r.json()["data"]["list"]):
                        assert i == districtCode
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getProvinceList()
        for provinceCode in getProvinceLists[0]:
            step_mgmt_sys_getCityList()
            for cityCode in getCityLists[0]:
                step_mgmt_sys_getRegionListByCity()
                for districtCode in getRegionListByCitys:
                    step_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("分页查询交通管制-成功路径: 查询乡镇街道检查")
    def test_04_mgmt_sys_traffic_queryTrafficControl(self):
        
        getProvinceLists = [] # 省份编码
        getCityLists = [] # 城市编码
        getRegionListByCitys = [] # 地区编码
        getStreetListByDistrictCodes = [] # 街道编码
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceLists                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getProvinceLists.append(d["code"])   

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": provinceCode, # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getCityLists.append(d["code"])  

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getRegionListByCity():
            
            nonlocal getRegionListByCitys
            params = {
                "cityCode": cityCode  # str城市编码
            }                   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getRegionListByCitys.append(d["code"])  

        @allure.step("根据城市编码获取下属街道")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            nonlocal getStreetListByDistrictCodes
            params = {
                "districtCode": districtCode  # str地区编码
            }                  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    getStreetListByDistrictCodes.append(d["code"])  

        @allure.step("分页查询交通管制：查询街道")
        def step_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)   
            data["provinceCode"] = provinceCode 
            data["cityCode"] = cityCode
            data["districtCode"] = districtCode
            data["streetCode"] = streetCode              
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in set(d["districtCode"] for d in r.json()["data"]["list"]):
                        assert i == districtCode
                else:
                    assert r.json()["data"]["list"] == []
        
        step_mgmt_sys_getProvinceList()
        for provinceCode in getProvinceLists[0]:
            step_mgmt_sys_getCityList()
            for cityCode in getCityLists[0]:
                step_mgmt_sys_getRegionListByCity()
                for districtCode in getRegionListByCitys[0]:
                    step_mgmt_sys_getStreetListByDistrictCode()
                    for streetCode in getStreetListByDistrictCodes:
                        step_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("分页查询交通管制-成功路径: 查询是否可发货检查")
    @pytest.mark.parametrize("wordsType,ids", [(0, "不可发货"), (1, "可发货但影响配送时效")])
    def test_05_mgmt_sys_traffic_queryTrafficControl(self, wordsType, ids):
        
        @allure.step("分页查询交通管制")
        def step_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)   
            data["wordsType"] = str(wordsType) # 0：不可发货 1：可发货但影响配送时效                
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["wordsType"] for d in r.json()["data"]["list"]):
                    assert i == wordsType      
        
        step_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("分页查询交通管制-成功路径: 查询状态检查")
    @pytest.mark.parametrize("trafficControlStatus,ids", [(0, "待生效"), (1, "生效"), (-1, "失效"), ])
    def test_06_mgmt_sys_traffic_queryTrafficControl(self, trafficControlStatus, ids):
        
        @allure.step("分页查询交通管制")
        def step_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)   
            data["provinceCode"] = str(trafficControlStatus) # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["trafficControlStatus"] for d in r.json()["data"]["list"]):
                    assert i == trafficControlStatus      
        
        step_mgmt_sys_traffic_queryTrafficControl()

