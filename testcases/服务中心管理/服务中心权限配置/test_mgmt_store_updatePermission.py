# coding:utf-8

from api.mall_mgmt_application._mgmt_store_updatePermission import data, _mgmt_store_updatePermission
from api.mall_mgmt_application._mgmt_store_getByParms import params, _mgmt_store_getByParms
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/updatePermission")
class TestClass:
    """
    服务中心权限编辑修改
    /mgmt/store/updatePermission
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("服务中心权限编辑修改-成功路径: 取消资格检查")
    def test_01_mgmt_store_updatePermission(self):
        
        @allure.step("根据常用条件查询服务中心: 点击【修改权限】按钮跳转")
        def step_mgmt_store_getByParms():
            
            params = deepcopy(self.params)
            params["storeCode"] = "903011"                
            with _mgmt_store_getByParms(params, self.access_token) as r:
                assert r.json()["data"][0]["code"] == params["storeCode"]
                self.storeCode = r.json()["data"][0]
       
        step_mgmt_store_getByParms()
        
        data = deepcopy(self.data)
        data["storeCode"] = self.storeCode["code"]
        data["storeName"] = self.storeCode["name"]
        data["leaderName"] = self.storeCode["leaderName"]
        data["cancelTime"] = int(round(time.time()*1000)) 
        data["permission"] = "3,7,6"
        data["businessMode"] = 1
        data["shopType"] = 12              
        with _mgmt_store_updatePermission(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == True
            assert r.json()["message"] == "操作成功"

    @allure.severity(P1)
    @allure.title("服务中心权限编辑修改-成功路径: 可押货+可交付+自购下单+可退货+代客下单检查")
    def test_02_mgmt_store_updatePermission(self):
        
        @allure.step("根据常用条件查询服务中心: 点击【修改权限】按钮跳转")
        def step_mgmt_store_getByParms():
            
            params = deepcopy(self.params)
            params["storeCode"] = "903011"                
            with _mgmt_store_getByParms(params, self.access_token) as r:
                assert r.json()["data"][0]["code"] == params["storeCode"]
                self.storeCode = r.json()["data"][0]
       
        step_mgmt_store_getByParms()
        
        data = deepcopy(self.data)
        data["storeCode"] = self.storeCode["code"]
        data["storeName"] = self.storeCode["name"]
        data["leaderName"] = self.storeCode["leaderName"]
        data["cancelTime"] = int(round(time.time()*1000)) 
        data["permission"] = "1,3,2,4,5"
        data["businessMode"] = 1
        data["shopType"] = 1             
        with _mgmt_store_updatePermission(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == True
            assert r.json()["message"] == "操作成功"










