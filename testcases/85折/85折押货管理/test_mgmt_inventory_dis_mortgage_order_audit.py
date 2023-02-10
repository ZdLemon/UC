# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_audit import data as data02, _mgmt_inventory_dis_mortgage_order_audit
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit import params, _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import data, _mgmt_inventory_dis_mortgage_order_mortgage
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/audit")
class TestClass:
    """
    押货单审核
    /mgmt/inventory/dis/mortgage/order/audit
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("押货单审核-成功路径: 审核通过检查")
    def test_01_mgmt_inventory_dis_mortgage_order_audit(self):
        
        orderId = None # 押货单id
        checkIsAuditAmountOverLimit = True # 是否超出库存限额
        
        @allure.step("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal orderId
            data = deepcopy(self.data)  
            data["transId"] = f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                orderId = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询押货单是否超出库存限额")
        def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
            
            nonlocal checkIsAuditAmountOverLimit
            params = deepcopy(self.params)
            params["orderId"] = orderId               
            with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, self.access_token) as r:
                checkIsAuditAmountOverLimit = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("审核通过押货单")
        def step_mgmt_inventory_dis_mortgage_order_audit():
            data = deepcopy(self.data02)
            data["orderId"] = orderId 
            data["auditRemarks"] = "同意押货单申请"
            data["auditResult"] = 1 # 审批结果 0不通过 1通过
            with _mgmt_inventory_dis_mortgage_order_audit(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        step_mgmt_inventory_dis_mortgage_order_mortgage()
        step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
        if checkIsAuditAmountOverLimit:
            raise Exception("超出库存限额 checkIsAuditAmountOverLimit = True")
        else:
            step_mgmt_inventory_dis_mortgage_order_audit()
            
    @allure.severity(P2)
    @allure.title("押货单审核-失败路径: 审核拒绝检查")
    def test_02_mgmt_inventory_dis_mortgage_order_audit(self):
        
        orderId = None # 押货单id
        checkIsAuditAmountOverLimit = True # 是否超出库存限额
        
        @allure.step("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal orderId
            data = deepcopy(self.data)  
            data["transId"] = f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676               
            with _mgmt_inventory_dis_mortgage_order_mortgage(data, self.access_token) as r:
                orderId = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("查询押货单是否超出库存限额")
        def step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit():
            
            nonlocal checkIsAuditAmountOverLimit
            params = deepcopy(self.params)
            params["orderId"] = orderId               
            with _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit(params, self.access_token) as r:
                checkIsAuditAmountOverLimit = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("审核拒绝押货单")
        def step_mgmt_inventory_dis_mortgage_order_audit():
            data = deepcopy(self.data02)
            data["orderId"] = orderId 
            data["auditRemarks"] = "拒绝押货单申请"
            data["auditResult"] = 0 # 审批结果 0不通过 1通过
            with _mgmt_inventory_dis_mortgage_order_audit(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        step_mgmt_inventory_dis_mortgage_order_mortgage()
        step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
        step_mgmt_inventory_dis_mortgage_order_audit()
            



