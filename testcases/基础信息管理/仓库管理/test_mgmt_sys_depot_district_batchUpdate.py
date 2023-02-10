# coding:utf-8

from api.mall_mgmt_application._mgmt_sys_depot_district_search import data, _mgmt_sys_depot_district_search # 查询仓库列表
from api.mall_center_sys._mgmt_sys_depot_list import _mgmt_sys_depot_list # 获取仓库信息集合
from api.mall_mgmt_application._mgmt_sys_depot_district_batchUpdate import _mgmt_sys_depot_district_batchUpdate # 批量修改区域对应仓库
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/sys/depot/district/batchUpdate")
class TestClass:
    """
    批量批量修改区域对应仓库
    /mgmt/sys/depot/district/batchUpdate
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("批量修改区域对应仓库-成功路径: 修改C区省份仓库区域检查")
    def test_01_mgmt_sys_depot_district_batchUpdate(self):
        
        district_search = {} # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 批量修改区域对应仓库
        provinceCode = "650000000000"
        
        @allure.step("查询仓库列表")
        def step_01_mgmt_sys_depot_district_search():
            
            nonlocal district_search
            data = deepcopy(self.data)
            data["provinceCode"] = provinceCode               
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    district_search = r.json()["data"][0]

        @allure.step("获取仓库信息集合")
        def step_mgmt_sys_depot_list():
            
            nonlocal depot_list                
            with _mgmt_sys_depot_list(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    depot_list = r.json()["data"]

        @allure.step("批量修改区域对应仓库")
        def step_mgmt_sys_depot_district_batchUpdate():
            
            nonlocal district_update
            data = {
                "provinceCode": provinceCode, # 省编码
                "cityCode":"", # 市编码
                "sysDepotCode": district_search["code"], # 仓库编码
                "businessRange": 2 # 区域
            }
            for i in depot_list:
                if i["businessRangeStr"] == "C" and i["code"] != district_search["code"]:
                    data["sysDepotCode"] = i["code"]
            with _mgmt_sys_depot_district_batchUpdate(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                district_update = data

        @allure.step("查询仓库列表:确认修改成功")
        def step_02_mgmt_sys_depot_district_search():
            
            data = deepcopy(self.data) 
            data["provinceCode"] = provinceCode         
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]:
                    assert i["code"] == district_update["sysDepotCode"]

        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_batchUpdate()
        step_02_mgmt_sys_depot_district_search()

    @allure.severity(P2)
    @allure.title("批量修改区域对应仓库-成功路径: 修改C区仓省份城市库状态检查")
    def test_02_mgmt_sys_depot_district_batchUpdate(self):
        
        district_search = {} # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 批量修改区域对应仓库
        provinceCode = "120000000000"
        cityCode = "120100000000"
        
        @allure.step("查询仓库列表")
        def step_01_mgmt_sys_depot_district_search():
            
            nonlocal district_search
            data = deepcopy(self.data)
            data["provinceCode"] = provinceCode
            data["cityCode"] = cityCode          
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    district_search = r.json()["data"][0]

        @allure.step("获取仓库信息集合")
        def step_mgmt_sys_depot_list():
            
            nonlocal depot_list                
            with _mgmt_sys_depot_list(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    depot_list = r.json()["data"]

        @allure.step("批量修改区域对应仓库")
        def step_mgmt_sys_depot_district_batchUpdate():
            
            nonlocal district_update
            data = {
                "provinceCode": provinceCode, # 省编码
                "cityCode": cityCode, # 市编码
                "sysDepotCode": district_search["code"], # 仓库编码
                "businessRange": 2 # 区域
            }
            for i in depot_list:
                if i["businessRangeStr"] == "C" and i["code"] != district_search["code"]:
                    data["sysDepotCode"] = i["code"]
            with _mgmt_sys_depot_district_batchUpdate(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                district_update = data

        @allure.step("查询仓库列表:确认修改成功")
        def step_02_mgmt_sys_depot_district_search():
            
            data = deepcopy(self.data) 
            data["provinceCode"] = provinceCode 
            data["cityCode"] = cityCode        
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]:
                    assert i["code"] == district_update["sysDepotCode"]

        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_batchUpdate()
        step_02_mgmt_sys_depot_district_search()

    @allure.severity(P2)
    @allure.title("批量修改区域对应仓库-成功路径: 修改B区仓库区域检查")
    def test_04_mgmt_sys_depot_district_batchUpdate(self):
        
        district_search = {} # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 批量修改区域对应仓库
        provinceCode = "130000000000"
        
        @allure.step("查询仓库列表")
        def step_01_mgmt_sys_depot_district_search():
            
            nonlocal district_search
            data = deepcopy(self.data)
            data["provinceCode"] = provinceCode
            data["businessRange"] = 1 # 业务范围: 1.B 2.C 3.B+C              
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    district_search = r.json()["data"][0]

        @allure.step("获取仓库信息集合")
        def step_mgmt_sys_depot_list():
            
            nonlocal depot_list                
            with _mgmt_sys_depot_list(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    depot_list = r.json()["data"]

        @allure.step("批量修改区域对应仓库")
        def step_mgmt_sys_depot_district_batchUpdate():
            
            nonlocal district_update
            data = {
                "provinceCode": provinceCode, # 省编码
                "cityCode":"", # 市编码
                "sysDepotCode": district_search["code"], # 仓库编码
                "businessRange": 1 # 区域
            }  
            for i in depot_list:
                if i["businessRangeStr"] == "B" and i["code"] != district_search["code"]:
                    data["sysDepotCode"] = i["code"]
            with _mgmt_sys_depot_district_batchUpdate(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                district_update = data

        @allure.step("查询仓库列表:确认修改成功")
        def step_02_mgmt_sys_depot_district_search():
            
            data = deepcopy(self.data) 
            data["provinceCode"] = provinceCode 
            data["businessRange"] = 1 # 业务范围: 1.B 2.C 3.B+C          
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]:
                    assert i["code"] == district_update["sysDepotCode"]
        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_batchUpdate()
        step_02_mgmt_sys_depot_district_search()

    @allure.severity(P2)
    @allure.title("批量修改区域对应仓库-成功路径: 修改B区仓省份城市库状态检查")
    def test_05_mgmt_sys_depot_district_batchUpdate(self):
        
        district_search = {} # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 批量修改区域对应仓库
        provinceCode = "130000000000"
        cityCode = "130100000000"
        
        @allure.step("查询仓库列表")
        def step_01_mgmt_sys_depot_district_search():
            
            nonlocal district_search
            data = deepcopy(self.data)
            data["provinceCode"] = provinceCode
            data["cityCode"] = cityCode
            data["businessRange"] = 1 # 业务范围: 1.B 2.C 3.B+C            
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    district_search = r.json()["data"][0]

        @allure.step("获取仓库信息集合")
        def step_mgmt_sys_depot_list():
            
            nonlocal depot_list                
            with _mgmt_sys_depot_list(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    depot_list = r.json()["data"]

        @allure.step("批量修改区域对应仓库")
        def step_mgmt_sys_depot_district_batchUpdate():
            
            nonlocal district_update
            data = {
                "provinceCode": provinceCode, # 省编码
                "cityCode": cityCode, # 市编码
                "sysDepotCode": district_search["code"], # 仓库编码
                "businessRange": 1 # 区域
            }
            for i in depot_list:
                if i["businessRangeStr"] == "B" and i["code"] != district_search["code"]:
                    data["sysDepotCode"] = i["code"]
            with _mgmt_sys_depot_district_batchUpdate(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                district_update = data

        @allure.step("查询仓库列表:确认修改成功")
        def step_02_mgmt_sys_depot_district_search():
            
            data = deepcopy(self.data) 
            data["provinceCode"] = provinceCode 
            data["cityCode"] = cityCode
            data["businessRange"] = 1 # 业务范围: 1.B 2.C 3.B+C          
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]:
                    assert i["code"] == district_update["sysDepotCode"]
        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_batchUpdate()
        step_02_mgmt_sys_depot_district_search()

                                 


