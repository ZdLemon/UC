# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_listPage import params, _mgmt_inventory_dis_mortgage_returnOrder_listPage
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/returnOrder/listPage")
class TestClass:
    """
    押货退货分页列表
    /mgmt/inventory/dis/mortgage/returnOrder/listPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("押货退货分页列表-成功路径: 查询默认条件检查")
    def test_01_mgmt_inventory_dis_mortgage_returnOrder_listPage(self):
        
        params = deepcopy(self.params)                
        with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("押货退货分页列表-成功路径: 查询服务中心编号检查")
    def test_02_mgmt_inventory_dis_mortgage_returnOrder_listPage(self):
        
        params = deepcopy(self.params) 
        params["storeCode"] = store_85               
        with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, self.access_token) as r:
            for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                assert i == store_85

