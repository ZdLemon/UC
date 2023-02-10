# coding:utf-8

import pytest
from api.basic_services._login import _login
from api.basic_services._login_oauth_token import _login_oauth_token

from setting import username_vip, username ,username_85, store, store_85, mysql_host, mysql_passwd, mysql_port, mysql_user, store, productCode_zh, productCode, couponNumber
from util.stepreruns import stepreruns
import os
from copy import deepcopy
import pymysql
 
import time
import uuid
import datetime
import calendar
import allure


@pytest.fixture(scope="function")
def addTrafficControl():
    "新增交通管制-海南"
    
    from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data as data01, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
    from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息
    from api.mall_center_sys._mgmt_sys_getCityList import _mgmt_sys_getCityList # 根据省份编码获取下属城市
    from api.mall_center_sys._mgmt_sys_getRegionListByCity import _mgmt_sys_getRegionListByCity # 根据城市编码获取下属地区
    from api.mall_center_sys._mgmt_sys_getStreetListByDistrictCode import _mgmt_sys_getStreetListByDistrictCode # 根据地区编码获取下属街道
    from api.mall_center_sys._mgmt_sys_traffic_addTrafficControl import _mgmt_sys_traffic_addTrafficControl # 添加交通管制
    
    access_token = os.environ["access_token"]
    getProvinceList = {} # 省份编码
    getCityLists = [] # 城市编码
    getRegionListByCitys = [] # 地区编码
    getStreetListByDistrictCodes = [] # 街道编码
    code = 500
            
    @allure.step("获取省份信息")
    def step_mgmt_sys_getProvinceList():
        
        nonlocal getProvinceList                     
        with _mgmt_sys_getProvinceList(access_token) as r:
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
        with _mgmt_sys_getCityList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCityLists = r.json()["data"] 

    @allure.step("根据城市编码获取下属地区")
    def step_mgmt_sys_getRegionListByCity():
        
        nonlocal getRegionListByCitys
        params = {
            "cityCode": getCityList["cityCode"]  # str城市编码
        }                   
        with _mgmt_sys_getRegionListByCity(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getRegionListByCitys = r.json()["data"]

    @allure.step("根据城市编码获取下属地区")
    def step_mgmt_sys_getStreetListByDistrictCode():
        
        nonlocal getStreetListByDistrictCodes
        params = {
            "districtCode": getRegionListByCity["districtCode"]  # str地区编码
        }                  
        with _mgmt_sys_getStreetListByDistrictCode(params, access_token) as r:
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
        with _mgmt_sys_traffic_addTrafficControl(data, access_token) as r:
            assert r.status_code == 200
            code = r.json()["code"]

    @allure.step("分页查询交通管制:确认生效")
    @stepreruns()
    def step_02_mgmt_sys_traffic_queryTrafficControl():
        
        data = deepcopy(data01)                     
        with _mgmt_sys_traffic_queryTrafficControl(data, access_token) as r:
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


@pytest.fixture(scope="function")
def addTrafficControl_2():
    "新增交通管制-新疆"
    
    from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data as data01, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
    from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息
    from api.mall_center_sys._mgmt_sys_getCityList import _mgmt_sys_getCityList # 根据省份编码获取下属城市
    from api.mall_center_sys._mgmt_sys_getRegionListByCity import _mgmt_sys_getRegionListByCity # 根据城市编码获取下属地区
    from api.mall_center_sys._mgmt_sys_getStreetListByDistrictCode import _mgmt_sys_getStreetListByDistrictCode # 根据地区编码获取下属街道
    from api.mall_center_sys._mgmt_sys_traffic_addTrafficControl import _mgmt_sys_traffic_addTrafficControl # 添加交通管制
    
    access_token = os.environ["access_token"]
    getProvinceList = {} # 省份编码
    getCityLists = [] # 城市编码
    getRegionListByCitys = [] # 地区编码
    getStreetListByDistrictCodes = [] # 街道编码
    code = 500
            
    @allure.step("获取省份信息")
    def step_mgmt_sys_getProvinceList():
        
        nonlocal getProvinceList                     
        with _mgmt_sys_getProvinceList(access_token) as r:
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
        with _mgmt_sys_getCityList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCityLists = r.json()["data"] 

    @allure.step("根据城市编码获取下属地区")
    def step_mgmt_sys_getRegionListByCity():
        
        nonlocal getRegionListByCitys
        params = {
            "cityCode": getCityList["cityCode"]  # str城市编码
        }                   
        with _mgmt_sys_getRegionListByCity(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getRegionListByCitys = r.json()["data"]

    @allure.step("根据城市编码获取下属地区")
    def step_mgmt_sys_getStreetListByDistrictCode():
        
        nonlocal getStreetListByDistrictCodes
        params = {
            "districtCode": getRegionListByCity["districtCode"]  # str地区编码
        }                  
        with _mgmt_sys_getStreetListByDistrictCode(params, access_token) as r:
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
        with _mgmt_sys_traffic_addTrafficControl(data, access_token) as r:
            assert r.status_code == 200
            code = r.json()["code"]

    @allure.step("分页查询交通管制:确认生效")
    @stepreruns()
    def step_02_mgmt_sys_traffic_queryTrafficControl():
        
        data = deepcopy(data01)                     
        with _mgmt_sys_traffic_queryTrafficControl(data, access_token) as r:
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



@pytest.fixture(scope="function")
def addTrafficControl_3():
    "新增交通管制定时生效-海南省"
    
    from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data as data01, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
    from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息
    from api.mall_center_sys._mgmt_sys_getCityList import _mgmt_sys_getCityList # 根据省份编码获取下属城市
    from api.mall_center_sys._mgmt_sys_getRegionListByCity import _mgmt_sys_getRegionListByCity # 根据城市编码获取下属地区
    from api.mall_center_sys._mgmt_sys_getStreetListByDistrictCode import _mgmt_sys_getStreetListByDistrictCode # 根据地区编码获取下属街道
    from api.mall_center_sys._mgmt_sys_traffic_addTrafficControl import _mgmt_sys_traffic_addTrafficControl # 添加交通管制
    
    access_token = os.environ["access_token"]
    getProvinceList = {} # 省份编码
    getCityLists = [] # 城市编码
    getRegionListByCitys = [] # 地区编码
    getStreetListByDistrictCodes = [] # 街道编码
    code = 500
    queryTrafficControl = {}
            
    @allure.step("获取省份信息")
    def step_mgmt_sys_getProvinceList():
        
        nonlocal getProvinceList                     
        with _mgmt_sys_getProvinceList(access_token) as r:
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
        with _mgmt_sys_getCityList(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getCityLists = r.json()["data"] 

    @allure.step("根据城市编码获取下属地区")
    def step_mgmt_sys_getRegionListByCity():
        
        nonlocal getRegionListByCitys
        params = {
            "cityCode": getCityList["cityCode"]  # str城市编码
        }                   
        with _mgmt_sys_getRegionListByCity(params, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            getRegionListByCitys = r.json()["data"]

    @allure.step("根据城市编码获取下属地区")
    def step_mgmt_sys_getStreetListByDistrictCode():
        
        nonlocal getStreetListByDistrictCodes
        params = {
            "districtCode": getRegionListByCity["districtCode"]  # str地区编码
        }                  
        with _mgmt_sys_getStreetListByDistrictCode(params, access_token) as r:
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
            "timeUp": int(round(datetime.datetime.timestamp(datetime.datetime.now()+datetime.timedelta(weeks=2)) * 1000)), # 定时生效时间
            "timeOff": "", # 定时失效时间
            "provinceName": getProvinceList["provinceName"], # 省
            "cityName": getCityList["cityName"], # 市
            "districtName": getRegionListByCity["districtName"], # 区
            "streetName": getStreetListByDistrictCode["streetName"], # 街道
            "stcwId": "1", # 交通管制提示语id
            "businessRange": 3 # 业务范围:1->B,2->C,3->B+C
        }                 
        with _mgmt_sys_traffic_addTrafficControl(data, access_token) as r:
            assert r.status_code == 200
            code = r.json()["code"]

    @allure.step("分页查询交通管制:确认海南是否有待生效的区域")
    def step_mgmt_sys_traffic_queryTrafficControl():
        
        nonlocal queryTrafficControl
        data = deepcopy(data01)
        data["provinceCode"] = getProvinceList["provinceCode"]
        data["trafficControlStatus"] = "0"                     
        with _mgmt_sys_traffic_queryTrafficControl(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                queryTrafficControl = r.json()["data"]["list"][0]
    
    @allure.step("分页查询交通管制:确认未到生效时间待生效")
    @stepreruns()
    def step_01_mgmt_sys_traffic_queryTrafficControl():
        
        data = deepcopy(data01)                     
        with _mgmt_sys_traffic_queryTrafficControl(data, access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["list"][0]["trafficControlStatus"] == 0 # 状态 1：生效 0：待生效（默认）-1：失效
                  
    step_mgmt_sys_getProvinceList()
    step_mgmt_sys_traffic_queryTrafficControl()
    if queryTrafficControl == {}:
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
