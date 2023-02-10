# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo import _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/returnOrder/searchAuditInfo")
class TestClass:
    """
    展示审批保存信息
    /mgmt/inventory/dis/mortgage/returnOrder/searchAuditInfo
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("展示审批保存信息-成功路径: 押货退货审批时展示审批保存信息检查")
    def test_mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(self):
                      
        with _mgmt_inventory_dis_mortgage_returnOrder_searchAuditInfo(self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
