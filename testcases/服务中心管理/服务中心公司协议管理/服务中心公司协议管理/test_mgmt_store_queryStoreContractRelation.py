# coding:utf-8

from api.mall_mgmt_application._mgmt_store_queryStoreContractRelation import params, _mgmt_store_queryStoreContractRelation
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    根据服务中心编号查询服务中心合同对接关联信息
    /mgmt/store/queryStoreContractRelation
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/store/queryStoreContractRelation")
    @allure.severity(P2)
    @allure.title("根据服务中心编号查询服务中心合同对接关联信息-成功路径: 查询已存在服务中心编号检查")
    def test_01_mgmt_store_queryStoreContractRelation(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = "902063"            
        with _mgmt_store_queryStoreContractRelation(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["storeCode"] == params["storeCode"]

    @allure.story("/mgmt/store/queryStoreContractRelation")
    @allure.severity(P3)
    @allure.title("根据服务中心编号查询服务中心合同对接关联信息-失败路径: 查询已存在服务中心编号的一部分检查")
    def test_02_mgmt_store_queryStoreContractRelation(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = "90206"            
        with _mgmt_store_queryStoreContractRelation(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 0
            assert r.json()["data"] == None
            assert r.json()["message"] == f"服务中心{params['storeCode']}未注册"
