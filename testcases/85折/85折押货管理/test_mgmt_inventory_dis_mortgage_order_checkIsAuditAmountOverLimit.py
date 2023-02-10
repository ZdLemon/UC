# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit import params, _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import data, _mgmt_inventory_dis_mortgage_order_mortgage
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/checkIsAuditAmountOverLimit")
class TestClass:
    """
    查询押货单是否超出库存限额
    /mgmt/inventory/dis/mortgage/order/checkIsAuditAmountOverLimit
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title(" 查询押货单是否超出库存限额-成功路径: 审核押货单时查询押货单是否超出库存限额检查")
    def test_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(self):
        
        orderId = None # 押货单id
        
        @allure.title("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal orderId
            data = deepcopy(self.data)                 
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                orderId = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询押货单是否超出库存限额")
        def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
            params = deepcopy(self.params)
            params["orderId"] = orderId               
            with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        step_mgmt_inventory_dis_mortgage_order_mortgage()
        step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()



