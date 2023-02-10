# coding:utf-8

from api.mall_mgmt_application._mgmt_store_checkBusinessAddressIsExist import params, _mgmt_store_checkBusinessAddressIsExist
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    检查经营地址是否存在，返回重复的服务中心编码，返回空则表示无重复
    /mgmt/store/checkBusinessAddressIsExist
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
        
    
    @allure.story("/mgmt/store/checkBusinessAddressIsExist")
    @allure.severity(P2)
    @allure.title("检查经营地址是否存在-成功路径: 经营地址不重复时返回None检查")
    def test_mgmt_store_checkBusinessAddressIsExist_01(self):
        
        params = deepcopy(self.params)
        with _mgmt_store_checkBusinessAddressIsExist(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == None

    @allure.story("/mgmt/store/checkBusinessAddressIsExist")
    @allure.severity(P3)
    @allure.title("检查经营地址是否存在-成功路径: 经营地址相同时检查(已取消资格的服务中心902002)")
    def test_mgmt_store_checkBusinessAddressIsExist_02(self):
        
        params = deepcopy(self.params)
        params = {
            "provinceName": "广东省",  # 省份
            "cityName": "佛山市",  # 城市
            "areaName": "三水区",  # 区县
            "streetName": "西南街道",  # 街道
            "detailAddress": "三兴路1号首层110"  #服务中心详细地址(门牌号)
        }
        with _mgmt_store_checkBusinessAddressIsExist(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "902002"

    @allure.story("/mgmt/store/checkBusinessAddressIsExist")
    @allure.severity(P3)
    @allure.title("检查经营地址是否存在-失败路径: 经营地址和942454的相同时返回重复的服务中心编码检查")
    def test_mgmt_store_checkBusinessAddressIsExist_03(self):
        
        params = deepcopy(self.params)
        params["detailAddress"] = "123号"      
        with _mgmt_store_checkBusinessAddressIsExist(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "942454"

    @allure.story("/mgmt/store/checkBusinessAddressIsExist")
    @allure.severity(P3)
    @allure.title("检查经营地址是否存在-失败路径: 经营地址和902012相同时返回重复的服务中心编码检查(没有街道值的特殊城市:中山市)")
    def test_mgmt_store_checkBusinessAddressIsExist_04(self):
        
        params = deepcopy(self.params)
        params = {
            "provinceName": "广东省",  # 省份
            "cityName": "中山市",  # 城市
            "areaName": "石岐区街道办事处",  # 区县
            "streetName": "",  # 街道
            "detailAddress": "东明路29号第五卡（经营地址）"  #服务中心详细地址(门牌号)
        }    
        with _mgmt_store_checkBusinessAddressIsExist(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == "902012"

