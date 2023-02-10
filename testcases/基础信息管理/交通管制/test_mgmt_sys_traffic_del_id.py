# coding:utf-8

from api.mall_center_sys._mgmt_sys_traffic_queryTrafficControl import data, _mgmt_sys_traffic_queryTrafficControl # 分页查询交通管制
from api.mall_center_sys._mgmt_sys_traffic_del_id import _mgmt_sys_traffic_del_id # 删除更新交通管制
from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息

from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_center_sys")
@allure.story("/mgmt/sys/traffic/del")
class TestClass:
    """
    删除更新交通管制
    /mgmt/sys/traffic/del/{id}
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("删除更新交通管制-成功路径: 删除更新交通管制检查")
    def test_01_mgmt_sys_traffic_del_id(self):
        
        ids = []
        getProvinceList = None # 省份编码

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
        def step_mgmt_sys_traffic_queryTrafficControl():
            
            nonlocal ids
            data = deepcopy(self.data)   
            data["trafficControlStatus"] = "-1" # 状态 1：生效 0：待生效（默认）-1：失效                    
            with _mgmt_sys_traffic_queryTrafficControl(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["list"]:
                    for i in r.json()["data"]["list"]:
                        ids.append(i["id"])
        
        @allure.step("删除更新交通管制")
        def step_mgmt_sys_traffic_del_id():
            
            params = {"id": id}                    
            with _mgmt_sys_traffic_del_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
       
        step_mgmt_sys_getProvinceList()
        step_mgmt_sys_traffic_queryTrafficControl()
        if ids:
            for id in ids:
                step_mgmt_sys_traffic_del_id()

