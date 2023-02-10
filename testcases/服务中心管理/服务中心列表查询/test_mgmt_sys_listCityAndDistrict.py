# coding:utf-8

from api.mall_center_sys._mgmt_sys_listCityAndDistrict import params, _mgmt_sys_listCityAndDistrict
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_center_sys")
class TestClass:
    """
    根据省份编码获取下属城市和地区信息
    /mgmt/sys/listCityAndDistrict
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/sys/listCityAndDistrict")
    @allure.severity(P2)
    @allure.title("根据省份编码获取下属城市和地区信息-成功路径: 新建服务中心时录入广东省检查")
    def test_mgmt_sys_listCityAndDistrict(self):
        
        params = deepcopy(self.params)  
        params["provinceCode"] = "440000000000"              
        with _mgmt_sys_listCityAndDistrict(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            assert len(r.json()["data"]) == 23
            assert r.json()["data"][0] == {
                "cityCode": "440100000000",
                "cityName": "广州市",
                "level": None,
                "districtList": [
                    {
                        "districtCode": "440103000000",
                        "districtName": "荔湾区"
                    }, 
                    {
                        "districtCode": "440104000000",
                        "districtName": "越秀区"
                    }, 
                    {
                        "districtCode": "440105000000",
                        "districtName": "海珠区"
                    }, 
                    {
                        "districtCode": "440106000000",
                        "districtName": "天河区"
                    }, 
                    {
                        "districtCode": "440111000000",
                        "districtName": "白云区"
                    }, 
                    {
                        "districtCode": "440112000000",
                        "districtName": "黄埔区"
                    }, 
                    {
                        "districtCode": "440113000000",
                        "districtName": "番禺区"
                    }, 
                    {
                        "districtCode": "440114000000",
                        "districtName": "花都区"
                    }, 
                    {
                        "districtCode": "440115000000",
                        "districtName": "南沙区"
                    }, 
                    {
                        "districtCode": "440117000000",
                        "districtName": "从化区"
                    },
                    {
                        "districtCode": "440118000000",
                        "districtName": "增城区"
                    }
                ]
            }
            
            
            
            
            
            
            