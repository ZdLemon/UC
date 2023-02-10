# coding:utf-8

from api.mall_mgmt_application._mgmt_store_addStore import data, _mgmt_store_addStore
from api.mall_center_sys._mgmt_sys_getProvinceList import _mgmt_sys_getProvinceList # 获取省份信息
from api.mall_mgmt_application._mgmt_store_leader_getLeaderByCardNo import params as params01, _mgmt_store_leader_getLeaderByCardNo # 根据会员卡号检查时候存在有效的总店
from api.mall_mgmt_application._mgmt_store_getMasterMemberInfoByCardNo import params as params02, _mgmt_store_getMasterMemberInfoByCardNo
from api.mall_mgmt_application._mgmt_store_checkStoreNameIsExist import params as params03, _mgmt_store_checkStoreNameIsExist
from api.mall_center_sys._mgmt_sys_listCityAndDistrict import params as params04, _mgmt_sys_listCityAndDistrict
from api.mall_center_sys._mgmt_sys_getRegionListByCity import params as params05, _mgmt_sys_getRegionListByCity
from api.mall_center_sys._mgmt_sys_getStreetListByDistrictCode import params as params06, _mgmt_sys_getStreetListByDistrictCode
from api.mall_mgmt_application._mgmt_store_checkBusinessAddressIsExist import params as params07, _mgmt_store_checkBusinessAddressIsExist
from api.mall_mgmt_application._mgmt_store_listStore import params as params08, _mgmt_store_listStore
from api.mall_mgmt_application._mgmt_store_getByParms import params as params09, _mgmt_store_getByParms
from api.mall_mgmt_application._mgmt_store_updatePermission import data as data02, _mgmt_store_updatePermission
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import time
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/addStore")
@pytest.mark.skip("避免创建太多的服务中心,用光编号")
class TestClass:
    """
    添加服务中心
    /mgmt/store/addStore
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
        self.params01 = deepcopy(params01)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.params04 = deepcopy(params04)
        self.params05 = deepcopy(params05)
        self.params06 = deepcopy(params06)
        self.params07 = deepcopy(params07)
        self.params08 = deepcopy(params08)
        self.params09 = deepcopy(params09)
        self.data02 = data02
    
    @allure.severity(P1)
    @allure.title("添加服务中心-成功路径: 云商新建总店检查")
    def test_01_mgmt_store_addStore(self):
        
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
               
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("根据会员卡号检查时候存在有效的总店")
        def step_mgmt_store_leader_getLeaderByCardNo():
            
            params = deepcopy(self.params01)
            params["cardNo"] = "3000003338"    
            with _mgmt_store_leader_getLeaderByCardNo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["del"] == 1
        
        @allure.step("根据会员卡号获取主顾客信息")
        def step_mgmt_store_getMasterMemberInfoByCardNo():
            
            params = deepcopy(self.params02)
            params["cardNo"] = "3000003338"    
            with _mgmt_store_getMasterMemberInfoByCardNo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.addMemberLeaderAo = r.json()["data"]

        @allure.step("检查服务中心名称是否存在")
        def step_mgmt_store_checkStoreNameIsExist():
            
            params = deepcopy(self.params03)
            params["storeName"] = "王杨服务中心二号店"    
            with _mgmt_store_checkStoreNameIsExist(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"

        @allure.step("根据省份编码获取下属城市和地区信息:广东省")
        def step_mgmt_sys_listCityAndDistrict():
            
            params = deepcopy(self.params04)
            params["provinceCode"] = "440000000000"    
            with _mgmt_sys_listCityAndDistrict(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.cityCode = r.json()["data"][0]["cityCode"]

        @allure.step("根据城市编码获取下属地区:广州市")
        def step_mgmt_sys_getRegionListByCity():
            
            params = deepcopy(self.params05)
            params["cityCode"] = self.cityCode   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.districtCode = r.json()["data"][2]["code"]

        @allure.step("根据地区编码获取下属街道:海珠区")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            params = deepcopy(self.params06)
            params["districtCode"] = self.districtCode  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.street = r.json()["data"][14]

        @allure.step("检查经营地址是否存在")
        def step_mgmt_store_checkBusinessAddressIsExist():
            
            params = deepcopy(self.params07)
            params["cityName"] = self.cityCode
            params["areaName"] = self.districtCode 
            params["streetName"] = self.street
            params["detailAddress"] = f"琶洲新村11号"  
            with _mgmt_store_checkBusinessAddressIsExist(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == None
            
            self.params07["detailAddress"] = params["detailAddress"]

        @allure.step("添加服务中心")
        def step_mgmt_store_addStore():
            
            data = deepcopy(self.data)
            data["addMemberLeaderAo"] = self.addMemberLeaderAo
            with _mgmt_store_addStore(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == True
                assert r.json()["message"] == "操作成功"

        @allure.step("获取服务中心列表: 通过负责人卡号搜索服务中心")
        def step_mgmt_store_listStore():
            params = deepcopy(self.params08)
            params["leaderCardNo"] = "3000003338"                 
            with _mgmt_store_listStore(params, self.access_token) as r:
                for d in r.json()["data"]["list"][0:-1]:
                    assert d["del"] == 1
                assert r.json()["data"]["list"][-1]["del"] == 0
                self.storeCode =  r.json()["data"]["list"][-1]["code"]


        @allure.step("根据常用条件查询服务中心: 点击[修改权限]按钮跳转")
        def step_mgmt_store_getByParms():
            
            params = deepcopy(self.params09)
            params["storeCode"] = self.storeCode              
            with _mgmt_store_getByParms(params, self.access_token) as r:
                assert r.json()["data"][0]["code"] == params["storeCode"]
                self.storeCode = r.json()["data"][0]
        
        @allure.step("服务中心权限编辑修改: 取消资格")
        def step_mgmt_store_updatePermission():
            
            data = deepcopy(self.data02)
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


        step_mgmt_sys_getProvinceList()
        step_mgmt_store_leader_getLeaderByCardNo()
        step_mgmt_store_getMasterMemberInfoByCardNo()
        step_mgmt_store_checkStoreNameIsExist()
        step_mgmt_sys_listCityAndDistrict()
        step_mgmt_sys_getRegionListByCity()
        step_mgmt_sys_getStreetListByDistrictCode()
        step_mgmt_store_checkBusinessAddressIsExist()
        step_mgmt_store_addStore()
        step_mgmt_store_listStore()
        step_mgmt_store_getByParms()
        step_mgmt_store_updatePermission()

    @allure.severity(P1)
    @allure.title("添加服务中心-成功路径: 云商新建85折服务中心-可押货+可押货退货+可代客下85折单+可自购85折单+可代客下单+可自购检查")
    def test_02_mgmt_store_addStore(self):
        
        @allure.step("获取省份信息")
        def step_mgmt_sys_getProvinceList():
               
            with _mgmt_sys_getProvinceList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("根据会员卡号检查时候存在有效的总店")
        def step_mgmt_store_leader_getLeaderByCardNo():
            
            params = deepcopy(self.params01)
            params["cardNo"] = "3000003338"    
            with _mgmt_store_leader_getLeaderByCardNo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["del"] == 1
        
        @allure.step("根据会员卡号获取主顾客信息")
        def step_mgmt_store_getMasterMemberInfoByCardNo():
            
            params = deepcopy(self.params02)
            params["cardNo"] = "3000003338"    
            with _mgmt_store_getMasterMemberInfoByCardNo(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.addMemberLeaderAo = r.json()["data"]

        @allure.step("检查服务中心名称是否存在")
        def step_mgmt_store_checkStoreNameIsExist():
            
            params = deepcopy(self.params03)
            params["storeName"] = "王杨服务中心二号店"    
            with _mgmt_store_checkStoreNameIsExist(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"

        @allure.step("根据省份编码获取下属城市和地区信息:广东省")
        def step_mgmt_sys_listCityAndDistrict():
            
            params = deepcopy(self.params04)
            params["provinceCode"] = "440000000000"    
            with _mgmt_sys_listCityAndDistrict(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.cityCode = r.json()["data"][0]["cityCode"]

        @allure.step("根据城市编码获取下属地区:广州市")
        def step_mgmt_sys_getRegionListByCity():
            
            params = deepcopy(self.params05)
            params["cityCode"] = self.cityCode   
            with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.districtCode = r.json()["data"][2]["code"]

        @allure.step("根据地区编码获取下属街道:海珠区")
        def step_mgmt_sys_getStreetListByDistrictCode():
            
            params = deepcopy(self.params06)
            params["districtCode"] = self.districtCode  
            with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                self.street = r.json()["data"][14]

        @allure.step("检查经营地址是否存在")
        def step_mgmt_store_checkBusinessAddressIsExist():
            
            params = deepcopy(self.params07)
            params["cityName"] = self.cityCode
            params["areaName"] = self.districtCode 
            params["streetName"] = self.street
            params["detailAddress"] = f"琶洲新村11号"  
            with _mgmt_store_checkBusinessAddressIsExist(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == None
            
            self.params07["detailAddress"] = params["detailAddress"]

        @allure.step("添加服务中心")
        def step_mgmt_store_addStore():
            
            data = deepcopy(self.data)
            data["addMemberLeaderAo"] = self.addMemberLeaderAo
            with _mgmt_store_addStore(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"] == True
                assert r.json()["message"] == "操作成功"

        @allure.step("获取服务中心列表: 通过负责人卡号搜索服务中心")
        def step_mgmt_store_listStore():
            params = deepcopy(self.params08)
            params["leaderCardNo"] = "3000003338"                 
            with _mgmt_store_listStore(params, self.access_token) as r:
                for d in r.json()["data"]["list"][0:-1]:
                    assert d["del"] == 1
                assert r.json()["data"]["list"][-1]["del"] == 0
                self.storeCode =  r.json()["data"]["list"][-1]["code"]


        @allure.step("根据常用条件查询服务中心: 点击[修改权限]按钮跳转")
        def step_mgmt_store_getByParms():
            
            params = deepcopy(self.params09)
            params["storeCode"] = self.storeCode              
            with _mgmt_store_getByParms(params, self.access_token) as r:
                assert r.json()["data"][0]["code"] == params["storeCode"]
                self.storeCode = r.json()["data"][0]
        
        @allure.step("服务中心权限编辑修改: 取消资格")
        def step_mgmt_store_updatePermission():
            
            data = deepcopy(self.data02)
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


        step_mgmt_sys_getProvinceList()
        step_mgmt_store_leader_getLeaderByCardNo()
        step_mgmt_store_getMasterMemberInfoByCardNo()
        step_mgmt_store_checkStoreNameIsExist()
        step_mgmt_sys_listCityAndDistrict()
        step_mgmt_sys_getRegionListByCity()
        step_mgmt_sys_getStreetListByDistrictCode()
        step_mgmt_store_checkBusinessAddressIsExist()
        step_mgmt_store_addStore()
        step_mgmt_store_listStore()
        step_mgmt_store_getByParms()
        step_mgmt_store_updatePermission()


