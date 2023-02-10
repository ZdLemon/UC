# coding:utf-8

from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
from api.mall_center_sys._mgmt_sys_traffic_updateTrafficControl import _mgmt_sys_traffic_updateTrafficControl # 更新交通管制

from util.stepreruns import stepreruns
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest
import datetime


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/traffic/updateTrafficControl")
class TestClass:
    """
    更新交通管制
    /mgmt/sys/traffic/updateTrafficControl
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P3)
    @allure.title("更新交通管制-成功路径: 编辑业务范围检查")
    @pytest.mark.parametrize("checkList,businessRange", [([1], 1), ([2], 2), ([1, 2], 3)])
    def test_01_mgmt_sys_traffic_updateTrafficControl(self, checkList, businessRange, addTrafficControl_3):
        
        id = None
        
        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal id
            data = deepcopy(self.data)
            data["trafficControlStatus"] = 1 # 状态 1：生效 0：待生效（默认）-1：失效                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("更新交通管制")
        def step_mgmt_sys_traffic_updateTrafficControl():
            
            data = {
                "checkList": checkList, # 业务范围 1：B区域，2：C区域
                "isControl": 1,
                "stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": int(round(datetime.datetime.timestamp(datetime.datetime.now()+datetime.timedelta(hours=1)) * 1000)), # 定时生效时间
                "timeOff": "", # 定时失效时间
                "stcwId": "1", # 交通管制提示语id
                "businessRange": businessRange, # 业务范围:1->B,2->C,3->B+C
                "id": id
            }                 
            with _mgmt_sys_traffic_updateTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("分页查询交通管制:确认更新成功")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data)
            data["trafficControlStatus"] = 0 # 状态 1：生效 0：待生效（默认）-1：失效                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["id"] == id:
                        assert i["businessRange"] == businessRange
          
        step_01_mgmt_sys_traffic_queryTrafficControl()
        if id:
            step_mgmt_sys_traffic_updateTrafficControl()
            step_02_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P3)
    @allure.title("更新交通管制-成功路径: 编辑是否可发货检查")
    @pytest.mark.parametrize("isControl,stcwId", [(1, "1"), (0, "2")])
    def test_02_mgmt_sys_traffic_updateTrafficControl(self, isControl, stcwId, addTrafficControl_3):
        
        id = None
        
        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal id
            data = deepcopy(self.data)
            data["trafficControlStatus"] = 1 # 状态 1：生效 0：待生效（默认）-1：失效                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
              
        @allure.step("更新交通管制")
        def step_mgmt_sys_traffic_updateTrafficControl():
            

            data = {
                "checkList": [1], # 业务范围 1：B区域，2：C区域
                "isControl": isControl, # 是否发货 0：不发货，1：发货
                "stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": int(round(datetime.datetime.timestamp(datetime.datetime.now()+datetime.timedelta(hours=1)) * 1000)), # 定时生效时间
                "timeOff": "", # 定时失效时间
                "stcwId": stcwId, # 交通管制提示语id
                "businessRange": 1, # 业务范围:1->B,2->C,3->B+C
                "id": id
            }                 
            with _mgmt_sys_traffic_updateTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data) 
            data["trafficControlStatus"] = 0 # 状态 1：生效 0：待生效（默认）-1：失效                                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in r.json()["data"]["list"]:
                    if i["id"] == id:
                        assert i["wordsType"] == isControl # 类型 0：不可发货 1：可发货但影响配送时效
          
        step_01_mgmt_sys_traffic_queryTrafficControl()
        if id:
            step_mgmt_sys_traffic_updateTrafficControl()
            step_02_mgmt_sys_traffic_queryTrafficControl()

    @allure.severity(P3)
    @allure.title("更新交通管制-成功路径: 编辑立即生效检查")
    def test_03_mgmt_sys_traffic_updateTrafficControl(self, addTrafficControl_3):
        
        id = None
        
        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_01_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal id
            data = deepcopy(self.data)
            data["trafficControlStatus"] = 1 # 状态 1：生效 0：待生效（默认）-1：失效                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
              
        @allure.step("更新交通管制")
        def step_mgmt_sys_traffic_updateTrafficControl():
            

            data = {
                "checkList": [1], # 业务范围 1：B区域，2：C区域
                "isControl": 1, # 是否发货 0：不发货，1：发货
                "stcType": 1, # 交通管理类型,1:立即生效; 2:定时生效;3:定时生效和失效
                "timeUp": "", # 定时生效时间
                "timeOff": "", # 定时失效时间
                "stcwId": "1", # 交通管制提示语id
                "businessRange": 1, # 业务范围:1->B,2->C,3->B+C
                "id": id
            }                 
            with _mgmt_sys_traffic_updateTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("分页查询交通管制:确认生效")
        @stepreruns()
        def step_02_mgmt_sys_traffic_queryTrafficControl():
            
            data = deepcopy(self.data) 
            data["trafficControlStatus"] = 1 # 状态 1：生效 0：待生效（默认）-1：失效                                     
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert id in set(d["id"] for d in r.json()["data"]["list"])
          
        step_01_mgmt_sys_traffic_queryTrafficControl()
        if id:
            step_mgmt_sys_traffic_updateTrafficControl()
            step_02_mgmt_sys_traffic_queryTrafficControl()




