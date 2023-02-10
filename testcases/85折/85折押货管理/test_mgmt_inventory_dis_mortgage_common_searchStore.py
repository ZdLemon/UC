# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import params, _mgmt_inventory_dis_mortgage_common_searchStore
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/common/searchStore")
class TestClass:
    """
    查询店铺信息
    /mgmt/inventory/dis/mortgage/common/searchStore
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("查询店铺信息-成功路径: 新建押货单时查询店铺信息检查")
    def test_mgmt_inventory_dis_mortgage_common_searchStore(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = store_85                   
        with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



