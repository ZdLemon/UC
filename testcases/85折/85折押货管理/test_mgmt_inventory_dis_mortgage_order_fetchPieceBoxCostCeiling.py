# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling import _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/fetchPieceBoxCostCeiling")
class TestClass:
    """
    获取启用中的拼箱费上限
    /mgmt/inventory/dis/mortgage/order/fetchPieceBoxCostCeiling
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("获取启用中的拼箱费上限-成功路径: 新建押货单时获取启用中的拼箱费上限检查")
    def test_mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(self):
                        
        with _mgmt_inventory_dis_mortgage_order_fetchPieceBoxCostCeiling(self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



