# coding:utf-8

from api.mall_mgmt_application._mgmt_store_leader_getLeaderByCardNo import params, _mgmt_store_leader_getLeaderByCardNo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    根据会员卡号获取服务中心负责人信息
    /mgmt/store/leader/getLeaderByCardNo
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/store/leader/getLeaderByCardNo")
    @allure.severity(P3)
    @allure.title("根据会员卡号获取服务中心负责人信息-失败路径: 查询已存在总店的会员检查")
    def test_01_mgmt_store_leader_getLeaderByCardNo(self):
        
        params = deepcopy(self.params)
        params["cardNo"] = "3000003480"            
        with _mgmt_store_leader_getLeaderByCardNo(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["del"] == 0
 
    @allure.story("/mgmt/store/leader/getLeaderByCardNo")
    @allure.severity(P2)
    @allure.title("根据会员卡号获取服务中心负责人信息-成功路径: 查询不存在总店的会员检查")
    def test_02_mgmt_store_leader_getLeaderByCardNo(self):
        
        params = deepcopy(self.params)
        params["cardNo"] = "3000003490"            
        with _mgmt_store_leader_getLeaderByCardNo(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"] is None

    @allure.story("/mgmt/store/leader/getLeaderByCardNo")
    @allure.severity(P2)
    @allure.title("根据会员卡号获取服务中心负责人信息-成功路径: 查询存在已取消资格的总店的会员检查")
    def test_03_mgmt_store_leader_getLeaderByCardNo(self):
        
        params = deepcopy(self.params)
        params["cardNo"] = "00004632"            
        with _mgmt_store_leader_getLeaderByCardNo(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["data"]["del"] == 1
