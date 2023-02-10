# coding:utf-8

from api.mall_mgmt_application._mgmt_sys_depot_district_search import data, _mgmt_sys_depot_district_search
from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/sys/depot/district/search")
class TestClass:
    """
    查询仓库列表
    /mgmt/sys/depot/district/search
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("查询仓库列表-成功路径: 查询省份检查")
    def test_01_mgmt_sys_depot_district_search(self):
        
        getProvinceList = [] # 获取省份信息
        
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
            
            nonlocal getProvinceList                  
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getProvinceList = r.json()["data"] 

        @allure.step("查询仓库列表")
        def step_02_mgmt_sys_depot_district_search():
            
            data = deepcopy(self.data)
            data["provinceCode"] = getProvince["provinceCode"]                  
            with _mgmt_sys_depot_district_search(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    for i in set(d["provinceName"] for d in r.json()["data"]):
                        assert i == getProvince["provinceName"]
        
        step_mgmt_sys_getProvinceList()
        for getProvince in getProvinceList:
            step_02_mgmt_sys_depot_district_search()

