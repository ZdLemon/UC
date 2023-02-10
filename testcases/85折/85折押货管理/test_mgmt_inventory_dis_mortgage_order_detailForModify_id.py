# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_audit import data as data02, _mgmt_inventory_dis_mortgage_order_audit
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit import params, _mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_mortgage import data, _mgmt_inventory_dis_mortgage_order_mortgage
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detailForModify_id import _mgmt_inventory_dis_mortgage_order_detailForModify_id
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_searchProductPage import params as params02, _mgmt_inventory_dis_mortgage_order_searchProductPage
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import pytest
import time


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/detailForModify/id")
class TestClass:
    """
    押货单详情(修改)
    /mgmt/inventory/dis/mortgage/order/detailForModify/{id}
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]

    @allure.severity(P1)
    @allure.title("押货单详情(修改)-成功路径: 押货单详情(修改)检查")
    def test_mgmt_inventory_dis_mortgage_order_detailForModify_id(self):
        
        orderId = None # 押货单id
        checkIsAuditAmountOverLimit = True # 是否超出库存限额
        searchProductPage = None # 商品信息
        detailForModify = None # 押货单详情
        
        @allure.title("关键字搜索可押货商品")
        def step_mgmt_inventory_dis_mortgage_order_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params02)
            params["storeCode"] = store_85
            params["keyword"] = productCode              
            with _mgmt_inventory_dis_mortgage_order_searchProductPage(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
        
        @allure.step("押货下单")
        def step_mgmt_inventory_dis_mortgage_order_mortgage():
            
            nonlocal orderId
            data = {
                "storeCode": store_85, 
                "isDelivery": 1, # 是否发货
                "remarks": "", # 押货单备注
                "productList": [{ # 押货单商品列表信息
                    "productCode": searchProductPage["productCode"], # 押货商品编码
                    "mortgagePrice": searchProductPage["mortgagePrice"], # 商品押货价
                    "mortgageNum": 2 # 押货商品数量
                }],
                "transId": f"{store_85}_{int(round(time.time() * 1000))}" # 业务id 902208_1649053566676
            }
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

        @allure.step("押货单详情-修改")
        def step_mgmt_inventory_dis_mortgage_order_detailForModify_id():
            
            nonlocal detailForModify
            params = {"id": orderId}           
            with _mgmt_inventory_dis_mortgage_order_detailForModify_id(params, self.access_token) as r:
                detailForModify = r.json()["data"]
                assert r.status_code == 200
                assert r.json()["code"] == 200

        step_mgmt_inventory_dis_mortgage_order_searchProductPage()
        step_mgmt_inventory_dis_mortgage_order_mortgage()
        step_mgmt_inventory_dis_mortgage_order_checkIsAuditAmountOverLimit()
        if checkIsAuditAmountOverLimit:
            raise Exception("超出库存限额 checkIsAuditAmountOverLimit = True")
        else:
            step_mgmt_inventory_dis_mortgage_order_audit()
        step_mgmt_inventory_dis_mortgage_order_detailForModify_id()






