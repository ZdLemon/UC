# coding:utf-8

from api.mall_center_sys._mgmt_sys_getRegionListByCity import params, _mgmt_sys_getRegionListByCity
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    根据城市编码获取下属地区
    /mgmt/sys/getRegionListByCity
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/sys/getRegionListByCity")
    @allure.severity(P2)
    @allure.title("根据城市编码获取下属地区-成功路径: 新建服务中心时录入广州市检查")
    def test_mgmt_sys_getRegionListByCity(self):
        
        params = deepcopy(self.params)  
        params["cityCode"] = "440100000000"              
        with _mgmt_sys_getRegionListByCity(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            assert len(r.json()["data"]) == 11
            assert r.json()["data"] == [
                {
                    "id": None,
                    "code": "440103000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "荔湾区",
                    "districtCode": "440103000000",
                    "districtId": "440103000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "22"
                }, 
                {
                    "id": None,
                    "code": "440104000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "越秀区",
                    "districtCode": "440104000000",
                    "districtId": "440104000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "18"
                }, 
                {
                    "id": None,
                    "code": "440105000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "海珠区",
                    "districtCode": "440105000000",
                    "districtId": "440105000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "18"
                }, 
                {
                    "id": None,
                    "code": "440106000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "天河区",
                    "districtCode": "440106000000",
                    "districtId": "440106000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "21"
                }, 
                {
                    "id": None,
                    "code": "440111000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "白云区",
                    "districtCode": "440111000000",
                    "districtId": "440111000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "22"
                }, 
                {
                    "id": None,
                    "code": "440112000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "黄埔区",
                    "districtCode": "440112000000",
                    "districtId": "440112000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "15"
                }, 
                {
                    "id": None,
                    "code": "440113000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "番禺区",
                    "districtCode": "440113000000",
                    "districtId": "440113000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "16"
                }, 
                {
                    "id": None,
                    "code": "440114000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "花都区",
                    "districtCode": "440114000000",
                    "districtId": "440114000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "10"
                }, 
                {
                    "id": None,
                    "code": "440115000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "南沙区",
                    "districtCode": "440115000000",
                    "districtId": "440115000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "9"
                }, 
                {
                    "id": None,
                    "code": "440117000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "从化区",
                    "districtCode": "440117000000",
                    "districtId": "440117000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "11"
                }, 
                {
                    "id": None,
                    "code": "440118000000",
                    "provinceId": None,
                    "provinceName": None,
                    "provinceCode": None,
                    "cityName": None,
                    "cityCode": None,
                    "cityId": None,
                    "districtName": "增城区",
                    "districtCode": "440118000000",
                    "districtId": "440118000000",
                    "streetName": None,
                    "streetId": None,
                    "streetCode": None,
                    "affiliatedCount": "11"
                }
            ]

            
            
            
            
            
            