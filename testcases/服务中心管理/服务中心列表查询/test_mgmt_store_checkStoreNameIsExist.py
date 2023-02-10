# coding:utf-8

from api.mall_mgmt_application._mgmt_store_checkStoreNameIsExist import params, _mgmt_store_checkStoreNameIsExist
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    检查服务中心名称是否存在, code=500时,存在相同值,提示语取message
    /mgmt/store/checkStoreNameIsExist
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/store/checkStoreNameIsExist")
    @allure.severity(P2)
    @allure.title("检查服务中心名称是否存在-成功路径: 录入新的服务中心名称检查")
    def test_01_mgmt_store_checkStoreNameIsExist(self):
        
        params = deepcopy(self.params)
        params["storeName"] = "天地服务中心"            
        with _mgmt_store_checkStoreNameIsExist(params, self.access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] == None

    @allure.story("/mgmt/store/checkStoreNameIsExist")
    @allure.severity(P3)
    @allure.title("检查服务中心名称是否存在-成功路径: 录入已存在的服务中心名称检查(该服务中心已经取消资格)")
    def test_02_mgmt_store_checkStoreNameIsExist(self):
        
        params = deepcopy(self.params)
        params["storeName"] = "佛山市三水区西南街健美莱商品信息咨询服务部"            
        with _mgmt_store_checkStoreNameIsExist(params, self.access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"

    @allure.story("/mgmt/store/checkStoreNameIsExist")
    @allure.severity(P3)
    @allure.title("检查服务中心名称是否存在-失败路径: 录入已存在的服务中心名称检查")
    def test_03_mgmt_store_checkStoreNameIsExist(self):
        
        params = deepcopy(self.params)
        params["storeName"] = "佛山市禅城区美之姿商品信息咨询服务部"            
        with _mgmt_store_checkStoreNameIsExist(params, self.access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 0
            assert r.json()["message"] == "服务中心名字已存在，服务中心编码[902001]"






