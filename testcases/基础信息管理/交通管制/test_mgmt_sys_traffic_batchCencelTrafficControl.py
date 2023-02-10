# coding:utf-8

from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
from api.mall_center_sys._mgmt_sys_traffic_batchCencelTrafficControl import _mgmt_sys_traffic_batchCencelTrafficControl # 批量取消交通管制
from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest

from util.stepreruns import stepreruns


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/traffic/batchCencelTrafficControl")
class TestClass:
    """
    批量取消交通管制
    /mgmt/sys/traffic/batchCencelTrafficControl
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("批量取消交通管制-成功路径: 单个取消交通管制-是否可发货检查")
    @pytest.mark.parametrize("stcwId,wordsType", [("1", 1), ("2", 0)])
    def test_01_mgmt_sys_traffic_batchCencelTrafficControl(self, addTrafficControl, stcwId, wordsType):
        
        id = None
        
        @allure.step("分页查询交通管制:获取id")
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal id
            data = deepcopy(self.data)   
            data["trafficControlStatus"] = "1" # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    id = r.json()["data"]["list"][0]["id"]  
        
        @allure.step("批量取消交通管制")
        def step_mgmt_sys_traffic_batchCencelTrafficControl():
            
            data = {
                "ids": [id], # 主键id集合
                "stcType": "",
                "stcwId": stcwId, # 交通管制提示语id
            }                  
            with _mgmt_sys_traffic_batchCencelTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
     
        @allure.step("分页查询交通管制:确认取消或降级成功")
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal id
            data = deepcopy(self.data)   
            data["trafficControlStatus"] = "1" # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in  r.json()["data"]["list"]:
                    if i["id"] == id:
                        assert i["wordsType"] == wordsType # 类型 0：不可发货 1：可发货但影响配送时效
                
        step_01_mgmt_sys_traffic_queryTrafficControl()
        if id:
            step_mgmt_sys_traffic_batchCencelTrafficControl()
            step_02_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("批量取消交通管制-成功路径: 单个取消交通管制-立即失效检查")
    def test_02_mgmt_sys_traffic_batchCencelTrafficControl(self, addTrafficControl):
        
        id = None
        
        @allure.step("分页查询交通管制:获取id")
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal id
            data = deepcopy(self.data)   
            data["trafficControlStatus"] = "1" # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    id = r.json()["data"]["list"][0]["id"]  
        
        @allure.step("批量取消交通管制")
        def step_mgmt_sys_traffic_batchCencelTrafficControl():
            
            data = {
                "ids": [id], # 主键id集合
                "stcType": 4, # 立即失效
                "stcwId": "1", # 交通管制提示语id
            }                  
            with _mgmt_sys_traffic_batchCencelTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
     
        @allure.step("分页查询交通管制:确认取消或降级成功")
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal id
            data = deepcopy(self.data)   
            data["trafficControlStatus"] = "-1" # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in  r.json()["data"]["list"]:
                    if i["id"] == id:
                        assert i["trafficControlStatus"] == -1
                
        step_01_mgmt_sys_traffic_queryTrafficControl()
        if id:
            step_mgmt_sys_traffic_batchCencelTrafficControl()
            step_02_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P2)
    @allure.title("批量取消交通管制-成功路径: 单个取消交通管制-立即失效检查")
    def test_03_mgmt_sys_traffic_batchCencelTrafficControl(self, addTrafficControl, addTrafficControl_2):
        
        getProvinceList = None # 省份编码
        ids = []
        
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList                   
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["provinceName"] == "海南省":
                        getProvinceList = d["provinceCode"] 
        
        @allure.step("分页查询交通管制:获取id")
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal ids
            data = deepcopy(self.data)
            data["provinceCode"] = getProvinceList
            data["trafficControlStatus"] = "1" # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        ids.append(i["id"])
        
        @allure.step("批量取消交通管制")
        def step_mgmt_sys_traffic_batchCencelTrafficControl():
            
            data = {
                "ids": ids, # 主键id集合
                "stcType": 4, # 立即失效
                "stcwId": "1", # 交通管制提示语id
            }                  
            with _mgmt_sys_traffic_batchCencelTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
     
        @allure.step("分页查询交通管制:确认取消或降级成功")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)   
            data["trafficControlStatus"] = "-1" # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in  r.json()["data"]["list"]:
                    if i["id"] == id:
                        assert i["trafficControlStatus"] == -1
                
        step_mgmt_sys_getProvinceList()
        step_01_mgmt_sys_traffic_queryTrafficControl()
        if ids:
            step_mgmt_sys_traffic_batchCencelTrafficControl()
            for id in ids:
                step_02_mgmt_sys_traffic_queryTrafficControl()

