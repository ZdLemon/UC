# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_book_items import _mgmt_inventory_book_items
from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params ,_mgmt_inventory_order_listMortgageOrder # 运营后台押货单列表查询
from api.mall_mgmt_application._mgmt_inventory_order_getOrderDetail import params as params02, _mgmt_inventory_order_getOrderDetail # 后台获取押货单详情
from api.mall_mgmt_application._mgmt_inventory_returnOrder_listOrder import params as params03, _mgmt_inventory_returnOrder_listOrder # 后台查询押货后台查询押货退货单列表
from api.mall_mgmt_application._mgmt_inventory_returnOrder_getOrderDetail import _mgmt_inventory_returnOrder_getOrderDetail # 后台押货退货单详情
from api.mall_mgmt_application._mgmt_order_return_getOrderReturnDetails import _mgmt_order_return_getOrderReturnDetails # 退货详情
from api.mall_mgmt_application._mgmt_order_orderList import _mgmt_order_orderList # 订单列表

from setting import P1, P2, P3, BASE_URL, productCode, productCode_title, store, username, store_85

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter

from util.stepreruns import stepreruns


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/book-items")
class TestClass:
    """
    查询实时库存台账明细：店铺后台押货，定制品押货，押货退货数据检查
    /mgmt/inventory/book-items
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台押货数据检查")
    def test_01_mgmt_inventory_book_items(self, purchase_commit):
        
        orderSn = purchase_commit
        id = None
        productVoList = None # 押货单产品信息
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("获取押货数量,押货产品")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal productVoList
            params = deepcopy(self.params02)
            params["orderId"] = id
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "businessId": orderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": productVoList["productNum"], # 增减值
                    "source": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "outIn": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台定制品押货数据检查")
    def test_02_mgmt_inventory_book_items(self, purchase_commitCusOrder):
        
        orderSn = purchase_commitCusOrder
        id = None
        productVoList = None # 押货单产品信息
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("获取押货数量,押货产品")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal productVoList
            params = deepcopy(self.params02)
            params["orderId"] = id
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productSecCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "businessId": orderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": productVoList["productNum"], # 增减值
                    "source": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "outIn": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台押货退货数据检查")
    def test_03_mgmt_inventory_book_items(self, purchaseReturnOrder):
         
        orderSn = purchaseReturnOrder
        id = None
        productVoList = None # 押货退货单产品信息
        
        @allure.step("获取退货单id")
        def step_mgmt_inventory_returnOrder_listOrder():
            
            nonlocal id
            params = deepcopy(self.params03)
            params["orderSn"] = orderSn
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]

        
        @allure.step("后台押货退货单详情")
        def step_mgmt_inventory_returnOrder_getOrderDetail():
            
            nonlocal productVoList
            params = {
                "orderId": id
            }
            with _mgmt_inventory_returnOrder_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList =  r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == -productVoList["productRealNum"] # 增减值
                # assert r.json()["data"][0]["source"] == 2 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 2 # 出入库：1入库 2出库
        
        step_mgmt_inventory_returnOrder_listOrder()
        step_mgmt_inventory_returnOrder_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台13押货转移数据检查")
    def test_04_mgmt_inventory_book_items(self, disInventoryTransfer_addTransfer):
         
        addTransferList, recordList = disInventoryTransfer_addTransfer # 库存列表:大于0的库存

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store_85, # 服务中心编号
                "productCode": addTransferList["serialNo"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == recordList["returnSn"] # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == -1 # 增减值
                # assert r.json()["data"][0]["source"] == 4 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 2 # 出入库：1入库 2出库
        
        step_mgmt_inventory_book_items()



@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/book-items")
class TestClass02:
    """
    查询实时库存台账明细：完美运营后台后台押货，仅调账不发货押货，押货修改，押货批量修改，押货欠货停发，押货退货,代客售后，13押货转移数据检查
    /mgmt/inventory/book-items
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货数据检查")
    def test_01_mgmt_inventory_book_items(self, auditMortgageOrder):
        
        orderSn = auditMortgageOrder
        id = None
        productVoList = None # 押货单产品信息
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("获取押货数量,押货产品")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal productVoList
            params = deepcopy(self.params02)
            params["orderId"] = id
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == productVoList["productNum"] # 增减值
                # assert r.json()["data"][0]["source"] == 1 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台仅调账不发货押货数据检查")
    def test_02_mgmt_inventory_book_items(self, auditMortgageOrder_isDelivery):
        
        orderSn = auditMortgageOrder_isDelivery
        id = None
        productVoList = None # 押货单产品信息
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            params["customFlag"] = 0
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("获取押货数量,押货产品")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal productVoList
            params = deepcopy(self.params02)
            params["orderId"] = id
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == productVoList["productNum"] # 增减值
                # assert r.json()["data"][0]["source"] == 1 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货修改数据检查")
    def test_03_mgmt_inventory_book_items(self, updateMortgageOrder):
        
        orderSn = updateMortgageOrder
        id = None
        productVoList = None # 押货单产品信息
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("获取押货数量,押货产品")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal productVoList
            params = deepcopy(self.params02)
            params["orderId"] = id
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == productVoList["productNum"] # 增减值
                # assert r.json()["data"][0]["source"] == 1 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货批量修改数据检查")
    @stepreruns()
    def test_04_mgmt_inventory_book_items(self, updateMortgageOrder_0):
        
        orderSn = updateMortgageOrder_0
        id = None
        productVoList = None # 押货单产品信息
        
        @allure.step("获取id")
        def step_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal id
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("获取押货数量,押货产品")
        def step_mgmt_inventory_order_getOrderDetail():
            
            nonlocal productVoList
            params = deepcopy(self.params02)
            params["orderId"] = id
            with _mgmt_inventory_order_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == productVoList["productNum"] # 增减值
                # assert r.json()["data"][0]["source"] == 1 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_inventory_order_listMortgageOrder()
        step_mgmt_inventory_order_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货欠货停发数据检查")
    def test_05_mgmt_inventory_book_items(self, updateMortgageOrder_1_0):
         
        returnOrderSn = updateMortgageOrder_1_0
        id = None
        productVoList = None # 押货退货单产品信息
        
        @allure.step("获取退货单id")
        def step_mgmt_inventory_returnOrder_listOrder():
            
            nonlocal id
            params = deepcopy(self.params03)
            params["orderSn"] = returnOrderSn
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]

        
        @allure.step("后台押货退货单详情")
        def step_mgmt_inventory_returnOrder_getOrderDetail():
            
            nonlocal productVoList
            params = {
                "orderId": id
            }
            with _mgmt_inventory_returnOrder_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList =  r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == returnOrderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == -productVoList["productRealNum"] # 增减值
                # assert r.json()["data"][0]["source"] == 2 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 2 # 出入库：1入库 2出库
        
        step_mgmt_inventory_returnOrder_listOrder()
        step_mgmt_inventory_returnOrder_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货退货数据检查")
    def test_06_mgmt_inventory_book_items(self, returnOrder_auditOrder):
         
        orderSn = returnOrder_auditOrder
        id = None
        productVoList = None # 押货退货单产品信息
        
        @allure.step("获取退货单id")
        def step_mgmt_inventory_returnOrder_listOrder():
            
            nonlocal id
            params = deepcopy(self.params03)
            params["orderSn"] = orderSn
            with _mgmt_inventory_returnOrder_listOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]

        
        @allure.step("后台押货退货单详情")
        def step_mgmt_inventory_returnOrder_getOrderDetail():
            
            nonlocal productVoList
            params = {
                "orderId": id
            }
            with _mgmt_inventory_returnOrder_getOrderDetail(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList =  r.json()["data"]["productVoList"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == -productVoList["productRealNum"] # 增减值
                # assert r.json()["data"][0]["source"] == 2 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 2 # 出入库：1入库 2出库
        
        step_mgmt_inventory_returnOrder_listOrder()
        step_mgmt_inventory_returnOrder_getOrderDetail()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台代客售后-押货库存数据检查")
    def test_07_mgmt_inventory_book_items(self, return_applyReturn):
         
        orderSn = return_applyReturn
        getOrderReturnDetails = None # 退货退款单产品信息
        
        @allure.step("退货详情")
        def step_mgmt_order_return_getOrderReturnDetails():
            
            nonlocal getOrderReturnDetails
            params = {
                "returnNo": orderSn, # 退货单号
            }
            with _mgmt_order_return_getOrderReturnDetails(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderReturnDetails = r.json()["data"]["orderReturnProducts"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": getOrderReturnDetails["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == getOrderReturnDetails["quantity"] # 增减值
                # assert r.json()["data"][0]["source"] == 4 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_order_return_getOrderReturnDetails()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台代客售后-隔月退货-押货库存数据检查")
    @pytest.mark.skipif(time.localtime(time.time()).tm_mday < 15, reason="超过15日,才是隔月退货")
    def test_08_mgmt_inventory_book_items(self, return_applyReturn_2):
         
        orderSn = return_applyReturn_2
        getOrderReturnDetails = None # 退货退款单产品信息
        
        @allure.step("退货详情")
        def step_mgmt_order_return_getOrderReturnDetails():
            
            nonlocal getOrderReturnDetails
            params = {
                "returnNo": orderSn, # 退货单号
            }
            with _mgmt_order_return_getOrderReturnDetails(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderReturnDetails = r.json()["data"]["orderReturnProducts"][0]

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": getOrderReturnDetails["productCode"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == orderSn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == getOrderReturnDetails["quantity"] # 增减值
                # assert r.json()["data"][0]["source"] == 4 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 1 # 出入库：1入库 2出库
        
        
        step_mgmt_order_return_getOrderReturnDetails()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台13押货转移数据检查")
    def test_09_mgmt_inventory_book_items(self, addTransfer):
         
        addTransferList, recordList = addTransfer # 库存列表:大于0的库存

        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store_85, # 服务中心编号
                "productCode": addTransferList["serialNo"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == recordList["returnSn"] # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == -1 # 增减值
                # assert r.json()["data"][0]["source"] == 4 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 2 # 出入库：1入库 2出库
        
        step_mgmt_inventory_book_items()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/book-items")
class TestClass03:
    """
    查询实时库存台账明细：商城购货，退单数据检查
    /mgmt/inventory/book-items
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 商城购货-押货库存数据检查")
    @stepreruns()
    def test_01_mgmt_inventory_book_items(self, walletPay_to_me):
         
        queryWalletPayOrder = walletPay_to_me
        productVoList = None # 订单产品信息
        
        @allure.step("订单列表")
        def step_mgmt_order_orderList():
            
            nonlocal productVoList
            params = {
                "pageNum": 1,
                "pageSize": 10,
                "orderStatusList": 2, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
                "orderNo": queryWalletPayOrder["orderNos"][0],
                "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
                "stockType": 2, # 库存类型 1->公司库存 2->押货库存 3->单位团购库存 4->展业包库存 5->85折押货库存
                "creatorCard": username,
                "productOrderType": 1, # 订货类型 1->产品订货 2->资料订货 3->订制品订货
                "isUpgrade": 0,
            }
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["list"][0]["orderProductVos"][0]


        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["serialNo"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == queryWalletPayOrder["orderNos"][0] # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == -productVoList["quantity"] # 增减值
                # assert r.json()["data"][0]["source"] == 3 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 2 # 出入库：1入库 2出库
        
        step_mgmt_order_orderList()
        step_mgmt_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 商城购货退货退款-押货库存数据检查")
    @stepreruns()
    def test_02_mgmt_inventory_book_items(self, walletPay_to_me_applyReturn):
        
        queryWalletPayOrder, applyReturn = walletPay_to_me_applyReturn
        productVoList = None # 押货单产品信息
        
        @allure.step("订单列表")
        def step_mgmt_order_orderList():
            
            nonlocal productVoList
            params = {
                "pageNum": 1,
                "pageSize": 10,
                "orderStatusList": 5, # 订单状态 -3->待支付定金 -2->待提交尾款 -1->待支付尾款 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
                "orderNo": queryWalletPayOrder["orderNos"][0],
                "orderType": 1, # 订单类型 1-正常订单 2->补报订单 3->调差订单 4->单位团购转分订单 5->85折转分订单 6->85折转分补报订单 7->预售订单
                "stockType": 2, # 库存类型 1->公司库存 2->押货库存 3->单位团购库存 4->展业包库存 5->85折押货库存
                "creatorCard": username,
                "productOrderType": 1, # 订货类型 1->产品订货 2->资料订货 3->订制品订货
                "isUpgrade": 0,
            }
            with _mgmt_order_orderList(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["list"][0]["orderProductVos"][0]


        @allure.step("查询实时库存台账明细")
        def step_mgmt_inventory_book_items(): 
            
            params = {
                "storeCode": store, # 服务中心编号
                "productCode": productVoList["serialNo"], # 产品编码
            }                    
            with _mgmt_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0]["businessId"] == applyReturn # 来源的 业务id （可能是押货id，可能是商城订单id）
                assert r.json()["data"][0]["diffNum"] == productVoList["quantity"] # 增减值
                # assert r.json()["data"][0]["source"] == 4 # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                assert r.json()["data"][0]["outIn"] == 1 # 出入库：1入库 2出库
        
        step_mgmt_order_orderList()
        step_mgmt_inventory_book_items()



