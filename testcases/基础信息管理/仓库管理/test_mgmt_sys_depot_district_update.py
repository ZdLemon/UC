# coding:utf-8

from api.mall_mgmt_application._mgmt_sys_depot_district_search import data, _mgmt_sys_depot_district_search # 查询仓库列表
from api.mall_center_sys._mgmt_sys_depot_list import _mgmt_sys_depot_list # 获取仓库信息集合
from api.mall_mgmt_application._mgmt_sys_depot_district_update import _mgmt_sys_depot_district_update # 修改区域对应仓库
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/sys/depot/district/update")
class TestClass:
    """
    修改区域对应仓库
    /mgmt/sys/depot/district/update
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("修改区域对应仓库-成功路径: 修改C区仓库区域检查")
    def test_01_mgmt_sys_depot_district_update(self):
        
        district_search = [] # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 修改区域对应仓库
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

        @allure.step("修改区域对应仓库")
        def step_mgmt_sys_depot_district_update():
            
            nonlocal district_update
            data = {
                "sysDepotCode": district_search["code"], # 仓库编码
                "id": district_search["id"], # 仓库区域id
                "sysDepotStatus": district_search["sysDepotStatus"] # 状态 1：生效 -1：失效
            }  
            for i in depot_list:
                if i["businessRangeStr"] == "C" and i["code"] != district_search["code"]:
                    data["sysDepotCode"] = i["code"]
            with _mgmt_sys_depot_district_update(data, self.access_token) as r:
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
                if r.json()["data"]:
                    for i in r.json()["data"]:
                        if i["id"] == district_search["id"]:
                            assert i["code"] == district_update["sysDepotCode"]
                            assert i["sysDepotStatus"] == district_search["sysDepotStatus"]
                    assert district_search["id"] in [i["id"] for i in r.json()["data"]]
        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_update()
        step_02_mgmt_sys_depot_district_search()

    @allure.severity(P2)
    @allure.title("修改区域对应仓库-成功路径: 修改C区仓库状态检查")
    def test_02_mgmt_sys_depot_district_update(self):
        
        district_search = [] # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 修改区域对应仓库
        provinceCode = "120000000000"
        
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

        @allure.step("修改区域对应仓库")
        def step_mgmt_sys_depot_district_update():
            
            nonlocal district_update
            data = {
                "sysDepotCode": district_search["code"], # 仓库编码
                "id": district_search["id"], # 仓库区域id
                "sysDepotStatus": -1 if district_search["sysDepotStatus"] == 1 else 1 # 状态 1：生效 -1：失效
            }  
            with _mgmt_sys_depot_district_update(data, self.access_token) as r:
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
                if r.json()["data"]:
                    for i in r.json()["data"]:
                        if i["id"] == district_search["id"]:
                            assert i["code"] == district_update["sysDepotCode"]
                            assert i["sysDepotStatus"] == district_update["sysDepotStatus"]
                    assert district_search["id"] in [i["id"] for i in r.json()["data"]]
        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_update()
        step_02_mgmt_sys_depot_district_search()

    @allure.severity(P2)
    @allure.title("修改区域对应仓库-成功路径: 修改B区仓库区域检查")
    def test_04_mgmt_sys_depot_district_update(self):
        
        district_search = [] # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 修改区域对应仓库
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

        @allure.step("修改区域对应仓库")
        def step_mgmt_sys_depot_district_update():
            
            nonlocal district_update
            data = {
                "sysDepotCode": district_search["code"], # 仓库编码
                "id": district_search["id"], # 仓库区域id
                "sysDepotStatus": district_search["sysDepotStatus"] # 状态 1：生效 -1：失效
            }  
            for i in depot_list:
                if i["businessRangeStr"] == "B" and i["code"] != district_search["code"]:
                    data["sysDepotCode"] = i["code"]
            with _mgmt_sys_depot_district_update(data, self.access_token) as r:
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
                if r.json()["data"]:
                    for i in r.json()["data"]:
                        if i["id"] == district_search["id"]:
                            assert i["code"] == district_update["sysDepotCode"]
                            assert i["sysDepotStatus"] == district_search["sysDepotStatus"]
                    assert district_search["id"] in [i["id"] for i in r.json()["data"]]
        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_update()
        step_02_mgmt_sys_depot_district_search()

    @allure.severity(P2)
    @allure.title("修改区域对应仓库-成功路径: 修改B区仓库状态检查")
    def test_05_mgmt_sys_depot_district_update(self):
        
        district_search = [] # 查询仓库列表
        depot_list = [] # 获取仓库信息集合
        district_update = None # 修改区域对应仓库
        provinceCode = "210000000000"
        
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

        @allure.step("修改区域对应仓库")
        def step_mgmt_sys_depot_district_update():
            
            nonlocal district_update
            data = {
                "sysDepotCode": district_search["code"], # 仓库编码
                "id": district_search["id"], # 仓库区域id
                "sysDepotStatus": -1 if district_search["sysDepotStatus"] == 1 else 1 # 状态 1：生效 -1：失效
            }  
            with _mgmt_sys_depot_district_update(data, self.access_token) as r:
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
                if r.json()["data"]:
                    for i in r.json()["data"]:
                        if i["id"] == district_search["id"]:
                            assert i["code"] == district_update["sysDepotCode"]
                            assert i["sysDepotStatus"] == district_update["sysDepotStatus"]
                    assert district_search["id"] in [i["id"] for i in r.json()["data"]]
        
        step_01_mgmt_sys_depot_district_search()
        step_mgmt_sys_depot_list()
        step_mgmt_sys_depot_district_update()
        step_02_mgmt_sys_depot_district_search()

                           


