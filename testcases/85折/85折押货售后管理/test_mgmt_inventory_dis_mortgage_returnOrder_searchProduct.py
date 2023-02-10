# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchProduct import params, _mgmt_inventory_dis_mortgage_returnOrder_searchProduct
from setting import P1, P2, P3, store_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/returnOrder/searchProduct")
class TestClass:
    """
    商品编码搜索退货商品信息
    /mgmt/inventory/dis/mortgage/returnOrder/searchProduct
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("商品编码搜索退货商品信息-成功路径: 押货退货时搜索商品检查")
    def test_mgmt_inventory_dis_mortgage_returnOrder_searchProduct(self):
        
        params = deepcopy(self.params)                
        with _mgmt_inventory_dis_mortgage_returnOrder_searchProduct(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json()["data"]["productCode"] == productCode
