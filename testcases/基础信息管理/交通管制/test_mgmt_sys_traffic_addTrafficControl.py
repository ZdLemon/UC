# coding:utf-8

from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息
from api.mall_center_sys._mgmt_sys_getCityList import _mgmt_sys_getCityList # 根据省份编码获取下属城市
from api.mall_center_sys._mgmt_sys_getRegionListByCity import _mgmt_sys_getRegionListByCity # 根据城市编码获取下属地区
from api.mall_center_sys._mgmt_sys_getStreetListByDistrictCode import _mgmt_sys_getStreetListByDistrictCode # 根据地区编码获取下属街道
from api.mall_center_sys._mgmt_sys_traffic_addTrafficControl import _mgmt_sys_traffic_addTrafficControl # 添加交通管制

from util.stepreruns import stepreruns
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest
import datetime


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/traffic/addTrafficControl")
class TestClass:
    """
    添加交通管制
    /mgmt/sys/traffic/addTrafficControl
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("添加交通管制-成功路径: 立即生效检查")
    def test_01_mgmt_sys_traffic_addTrafficControl(self):
        
        getProvinceList = {} # 省份编码
        getCityLists = [] # 城市编码
        getRegionListByCitys = [] # 地区编码
        getStreetListByDistrictCodes = [] # 街道编码
        code = 500
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["provinceName"] == "海南省":
                        getProvinceList = d 

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": getProvinceList["provinceCode"], # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCityLists = r.json()["data"] 

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getRegionListByCity():
            
            nonlocal getRegionListByCitys
            params = {
                "cityCode": getCityList["cityCode"]  # str城市编码
            }                   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getRegionListByCitys = r.json()["data"]

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            nonlocal getStreetListByDistrictCodes
            params = {
                "districtCode": getRegionListByCity["districtCode"]  # str地区编码
            }                  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStreetListByDistrictCodes = r.json()["data"]  

        @allure.step("添加交通管制")
        def step_mgmt_sys_traffic_addTrafficControl():
            
            nonlocal code
            data = {
                "provinceCode": getProvinceList["provinceCode"], # 省编码
                "cityCode": getCityList["cityCode"], # 市编码
                "districtCode": getRegionListByCity["districtCode"], # 区县编码
                "streetCode": getStreetListByDistrictCode["streetCode"], # 街道编码
                "checkList": [1],
                "isControl": 1,
                "stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": "", # 定时生效时间
                "timeOff": "", # 定时失效时间
                "provinceName": getProvinceList["provinceName"], # 省
                "cityName": getCityList["cityName"], # 市
                "districtName": getRegionListByCity["districtName"], # 区
                "streetName": getStreetListByDistrictCode["streetName"], # 街道
                "stcwId": "1", # 交通管制提示语id
                "businessRange": 1 # 业务范围:1->B,2->C,3->B+C
            }                 
            with _mgmt_sys_traffic_addTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]

        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == 1 # 状态 1：生效 0：待生效（默认）-1：失效
          
        step_mgmt_sys_getProvinceList()
        step_mgmt_sys_getCityList()
        for getCityList in getCityLists:
            step_mgmt_sys_getRegionListByCity()
            for getRegionListByCity in getRegionListByCitys:
                step_mgmt_sys_getStreetListByDistrictCode()
                for getStreetListByDistrictCode in getStreetListByDistrictCodes:
                    step_mgmt_sys_traffic_addTrafficControl()
                    if code == 200:
                        break
                if code == 200:
                    break
            if code == 200:
                break
        step_02_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("添加交通管制-成功路径: 定时生效检查")
    def test_02_mgmt_sys_traffic_addTrafficControl(self):
        
        getProvinceList = {} # 省份编码
        getCityLists = [] # 城市编码
        getRegionListByCitys = [] # 地区编码
        getStreetListByDistrictCodes = [] # 街道编码
        code = 500
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["provinceName"] == "新疆维吾尔自治区":
                        getProvinceList = d 

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": getProvinceList["provinceCode"], # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCityLists = r.json()["data"] 

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getRegionListByCity():
            
            nonlocal getRegionListByCitys
            params = {
                "cityCode": getCityList["cityCode"]  # str城市编码
            }                   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getRegionListByCitys = r.json()["data"]

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            nonlocal getStreetListByDistrictCodes
            params = {
                "districtCode": getRegionListByCity["districtCode"]  # str地区编码
            }                  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStreetListByDistrictCodes = r.json()["data"]  

        @allure.step("添加交通管制")
        def step_mgmt_sys_traffic_addTrafficControl():
            
            nonlocal code
            data = {
                "provinceCode": getProvinceList["provinceCode"], # 省编码
                "cityCode": getCityList["cityCode"], # 市编码
                "districtCode": getRegionListByCity["districtCode"], # 区县编码
                "streetCode": getStreetListByDistrictCode["streetCode"], # 街道编码
                "checkList": [1, 2],
                "isControl": 1,
                "stcType": 2, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": int(round(datetime.datetime.timestamp(datetime.datetime.now()+datetime.timedelta(seconds=3)) * 1000)), # 定时生效时间
                "timeOff": "", # 定时失效时间
                "provinceName": getProvinceList["provinceName"], # 省
                "cityName": getCityList["cityName"], # 市
                "districtName": getRegionListByCity["districtName"], # 区
                "streetName": getStreetListByDistrictCode["streetName"], # 街道
                "stcwId": "1", # 交通管制提示语id
                "businessRange": 3 # 业务范围:1->B,2->C,3->B+C
            }                 
            with _mgmt_sys_traffic_addTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]

        @allure.step("分页查询交通管制:确认未到生效时间待生效")
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == 0 # 状态 1：生效 0：待生效（默认）-1：失效
        
        @allure.step("分页查询交通管制:确认到生效时间后生效")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == 1 # 状态 1：生效 0：待生效（默认）-1：失效
                        
        step_mgmt_sys_getProvinceList()
        step_mgmt_sys_getCityList()
        for getCityList in getCityLists:
            step_mgmt_sys_getRegionListByCity()
            for getRegionListByCity in getRegionListByCitys:
                step_mgmt_sys_getStreetListByDistrictCode()
                for getStreetListByDistrictCode in getStreetListByDistrictCodes:
                    step_mgmt_sys_traffic_addTrafficControl()
                    if code == 200:
                        break
                if code == 200:
                    break
            if code == 200:
                break
        step_01_mgmt_sys_traffic_queryTrafficControl()
        step_02_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("添加交通管制-成功路径: 定时生效失效检查")
    def test_03_mgmt_sys_traffic_addTrafficControl(self):
        
        getProvinceList = {} # 省份编码
        getCityLists = [] # 城市编码
        getRegionListByCitys = [] # 地区编码
        getStreetListByDistrictCodes = [] # 街道编码
        code = 500
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["provinceName"] == "新疆维吾尔自治区":
                        getProvinceList = d 

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": getProvinceList["provinceCode"], # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCityLists = r.json()["data"] 

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getRegionListByCity():
            
            nonlocal getRegionListByCitys
            params = {
                "cityCode": getCityList["cityCode"]  # str城市编码
            }                   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getRegionListByCitys = r.json()["data"]

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            nonlocal getStreetListByDistrictCodes
            params = {
                "districtCode": getRegionListByCity["districtCode"]  # str地区编码
            }                  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStreetListByDistrictCodes = r.json()["data"]  

        @allure.step("添加交通管制")
        def step_mgmt_sys_traffic_addTrafficControl():
            
            nonlocal code
            data = {
                "provinceCode": getProvinceList["provinceCode"], # 省编码
                "cityCode": getCityList["cityCode"], # 市编码
                "districtCode": getRegionListByCity["districtCode"], # 区县编码
                "streetCode": getStreetListByDistrictCode["streetCode"], # 街道编码
                "checkList": [2], # 业务范围 1：B区域，2：C区域
                "isControl": 0, # 是否发货 0：不发货，1：发货
                "stcType": 3, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": int(round(datetime.datetime.timestamp(datetime.datetime.now()+datetime.timedelta(seconds=2)) * 1000)), # 定时生效时间
                "timeOff": int(round(datetime.datetime.timestamp(datetime.datetime.now()+datetime.timedelta(seconds=5)) * 1000)), # 定时失效时间
                "provinceName": getProvinceList["provinceName"], # 省
                "cityName": getCityList["cityName"], # 市
                "districtName": getRegionListByCity["districtName"], # 区
                "streetName": getStreetListByDistrictCode["streetName"], # 街道
                "stcwId": "2", # 交通管制提示语id
                "businessRange": 2 # 业务范围:1->B,2->C,3->B+C
            }                 
            with _mgmt_sys_traffic_addTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]

        @allure.step("分页查询交通管制:确认未到生效时间待生效")
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == 0 # 状态 1：生效 0：待生效（默认）-1：失效
        
        @allure.step("分页查询交通管制:确认到生效时间后生效")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == 1 # 状态 1：生效 0：待生效（默认）-1：失效

        @allure.step("分页查询交通管制:确认到失效时间后失效")
        @stepreruns()
        def step_03_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == -1 # 状态 1：生效 0：待生效（默认）-1：失效
                        
        step_mgmt_sys_getProvinceList()
        step_mgmt_sys_getCityList()
        for getCityList in getCityLists:
            step_mgmt_sys_getRegionListByCity()
            for getRegionListByCity in getRegionListByCitys:
                step_mgmt_sys_getStreetListByDistrictCode()
                for getStreetListByDistrictCode in getStreetListByDistrictCodes:
                    step_mgmt_sys_traffic_addTrafficControl()
                    if code == 200:
                        break
                if code == 200:
                    break
            if code == 200:
                break
        step_01_mgmt_sys_traffic_queryTrafficControl()
        step_02_mgmt_sys_traffic_queryTrafficControl()
        step_03_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P3)
    @allure.title("添加交通管制-成功路径: 添加时业务范围检查")
    @pytest.mark.parametrize("checkList,businessRange", [([1], 1), ([2], 2), ([1, 2], 3)])
    def test_04_mgmt_sys_traffic_addTrafficControl(self, checkList, businessRange):
        
        getProvinceList = {} # 省份编码
        getCityLists = [] # 城市编码
        getRegionListByCitys = [] # 地区编码
        getStreetListByDistrictCodes = [] # 街道编码
        code = 500
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["provinceName"] == "海南省":
                        getProvinceList = d 

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": getProvinceList["provinceCode"], # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCityLists = r.json()["data"] 

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getRegionListByCity():
            
            nonlocal getRegionListByCitys
            params = {
                "cityCode": getCityList["cityCode"]  # str城市编码
            }                   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getRegionListByCitys = r.json()["data"]

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            nonlocal getStreetListByDistrictCodes
            params = {
                "districtCode": getRegionListByCity["districtCode"]  # str地区编码
            }                  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStreetListByDistrictCodes = r.json()["data"]  

        @allure.step("添加交通管制")
        def step_mgmt_sys_traffic_addTrafficControl():
            
            nonlocal code
            data = {
                "provinceCode": getProvinceList["provinceCode"], # 省编码
                "cityCode": getCityList["cityCode"], # 市编码
                "districtCode": getRegionListByCity["districtCode"], # 区县编码
                "streetCode": getStreetListByDistrictCode["streetCode"], # 街道编码
                "checkList": checkList, # 业务范围 1：B区域，2：C区域
                "isControl": 1,
                "stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": "", # 定时生效时间
                "timeOff": "", # 定时失效时间
                "provinceName": getProvinceList["provinceName"], # 省
                "cityName": getCityList["cityName"], # 市
                "districtName": getRegionListByCity["districtName"], # 区
                "streetName": getStreetListByDistrictCode["streetName"], # 街道
                "stcwId": "1", # 交通管制提示语id
                "businessRange": businessRange # 业务范围:1->B,2->C,3->B+C
            }                 
            with _mgmt_sys_traffic_addTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]

        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == 1 # 状态 1：生效 0：待生效（默认）-1：失效
          
        step_mgmt_sys_getProvinceList()
        step_mgmt_sys_getCityList()
        for getCityList in getCityLists:
            step_mgmt_sys_getRegionListByCity()
            for getRegionListByCity in getRegionListByCitys:
                step_mgmt_sys_getStreetListByDistrictCode()
                for getStreetListByDistrictCode in getStreetListByDistrictCodes:
                    step_mgmt_sys_traffic_addTrafficControl()
                    if code == 200:
                        break
                if code == 200:
                    break
            if code == 200:
                break
        step_02_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P3)
    @allure.title("添加交通管制-成功路径: 添加时是否可发货检查")
    @pytest.mark.parametrize("isControl,stcwId", [(1, "1"), (0, "2")])
    def test_04_mgmt_sys_traffic_addTrafficControl(self, isControl, stcwId):
        
        getProvinceList = {} # 省份编码
        getCityLists = [] # 城市编码
        getRegionListByCitys = [] # 地区编码
        getStreetListByDistrictCodes = [] # 街道编码
        code = 500
                
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList                     
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["provinceName"] == "海南省":
                        getProvinceList = d 

        @allure.step("根据省份编码获取下属城市")
        def step_mgmt_sys_getCityList():
            
            nonlocal getCityLists
            params = {
                "provinceCode": getProvinceList["provinceCode"], # 省份编码
            }                   
            with _mgmt_sys_getCityList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCityLists = r.json()["data"] 

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getRegionListByCity():
            
            nonlocal getRegionListByCitys
            params = {
                "cityCode": getCityList["cityCode"]  # str城市编码
            }                   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getRegionListByCitys = r.json()["data"]

        @allure.step("根据城市编码获取下属地区")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            nonlocal getStreetListByDistrictCodes
            params = {
                "districtCode": getRegionListByCity["districtCode"]  # str地区编码
            }                  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getStreetListByDistrictCodes = r.json()["data"]  

        @allure.step("添加交通管制")
        def step_mgmt_sys_traffic_addTrafficControl():
            
            nonlocal code
            data = {
                "provinceCode": getProvinceList["provinceCode"], # 省编码
                "cityCode": getCityList["cityCode"], # 市编码
                "districtCode": getRegionListByCity["districtCode"], # 区县编码
                "streetCode": getStreetListByDistrictCode["streetCode"], # 街道编码
                "checkList": [1], # 业务范围 1：B区域，2：C区域
                "isControl": isControl, # 是否发货 0：不发货，1：发货
                "stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": "", # 定时生效时间
                "timeOff": "", # 定时失效时间
                "provinceName": getProvinceList["provinceName"], # 省
                "cityName": getCityList["cityName"], # 市
                "districtName": getRegionListByCity["districtName"], # 区
                "streetName": getStreetListByDistrictCode["streetName"], # 街道
                "stcwId": stcwId, # 交通管制提示语id
                "businessRange": 1 # 业务范围:1->B,2->C,3->B+C
            }                 
            with _mgmt_sys_traffic_addTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                code = r.json()["code"]

        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"][0]["trafficControlStatus"] == 1 # 状态 1：生效 0：待生效（默认）-1：失效
          
        step_mgmt_sys_getProvinceList()
        step_mgmt_sys_getCityList()
        for getCityList in getCityLists:
            step_mgmt_sys_getRegionListByCity()
            for getRegionListByCity in getRegionListByCitys:
                step_mgmt_sys_getStreetListByDistrictCode()
                for getStreetListByDistrictCode in getStreetListByDistrictCodes:
                    step_mgmt_sys_traffic_addTrafficControl()
                    if code == 200:
                        break
                if code == 200:
                    break
            if code == 200:
                break
        step_02_mgmt_sys_traffic_queryTrafficControl()




