# coding:utf-8

from api.mall_center_sys._mgmt_sys_getStreetListByDistrictCode import params, _mgmt_sys_getStreetListByDistrictCode
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    根据地区编码获取下属街道
    /mgmt/sys/getStreetListByDistrictCode
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/sys/getStreetListByDistrictCode")
    @allure.severity(P2)
    @allure.title("根据地区编码获取下属街道-成功路径: 新建服务中心时录入广州市海珠区检查")
    def test_01_mgmt_sys_getStreetListByDistrictCode(self):
        
        params = deepcopy(self.params)  
        params["districtCode"] = "440105000000"              
        with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            assert len(r.json()["data"]) == 18
            assert r.json()["data"][14] == {
                "id": None,
                "code": "440105015000",
                "provinceId": None,
                "provinceName": None,
                "provinceCode": None,
                "cityName": None,
                "cityCode": None,
                "cityId": None,
                "districtName": None,
                "districtCode": None,
                "districtId": None,
                "streetName": "琶洲街道",
                "streetId": "440105015000",
                "streetCode": "440105015000",
                "affiliatedCount": None
            }
            
    @allure.story("/mgmt/sys/getStreetListByDistrictCode")
    @allure.severity(P3)
    @allure.title("根据地区编码获取下属街道-失败路径: 新建服务中心时录入中山市石岐区检查(没有街道的特殊城市)")
    def test_02_mgmt_sys_getStreetListByDistrictCode(self):
        
        params = deepcopy(self.params)  
        params["districtCode"] = "442000001000"              
        with _mgmt_sys_getStreetListByDistrictCode(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            assert r.json()["data"] == []

            
                        
            