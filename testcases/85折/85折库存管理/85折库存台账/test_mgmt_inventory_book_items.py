# coding:utf-8

from api.mall_mgmt_application._mgmt_dis_inventory_book_items import params, _mgmt_dis_inventory_book_items # 查询实时库存台账明细
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_listPage import params as params03, _mgmt_inventory_dis_mortgage_order_listPage # 押货单列表查询
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_detail_id import _mgmt_inventory_dis_mortgage_order_detail_id # 押货单详情
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_listPage import params as params02, _mgmt_inventory_dis_mortgage_returnOrder_listPage # 押货退货列表
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_detail_id import _mgmt_inventory_dis_mortgage_returnOrder_detail_id # 押货退货单详情

from setting import P1, P2, P3, productCode, productCode_title, store_85

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
    查询实时库存台账明细:完美运营后台押货，仅调账不发货押货单，押货修改，欠货不发，押货退货，套装组合，拆分，代客售后，13押货转移数据检查
    /mgmt/dis-inventory/book-items
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货单数据检查")
    def test_01_mgmt_dis_inventory_book_items(self, order_mortgage):
            
        orderSn, payAmount, orderId = order_mortgage
        productVoList = None # 押货单产品信息
        
        @allure.step("获取押货单信息")
        def step_mgmt_inventory_dis_mortgage_order_detail_id():
            
            nonlocal productVoList
            params = {"id": orderId}
            with _mgmt_inventory_dis_mortgage_order_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
            
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": orderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": productVoList["mortgageNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_order_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台仅调账不发货押货单数据检查")
    def test_02_mgmt_dis_inventory_book_items(self, order_mortgage_isDelivery):
            
        orderSn, payAmount, orderId = order_mortgage_isDelivery
        productVoList = None # 押货单产品信息
        
        @allure.step("获取押货单信息")
        def step_mgmt_inventory_dis_mortgage_order_detail_id():
            
            nonlocal productVoList
            params = {"id": orderId}
            with _mgmt_inventory_dis_mortgage_order_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
            
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": orderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": productVoList["mortgageNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_order_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货单修改数据检查")
    def test_03_mgmt_dis_inventory_book_items(self, order_modify):
            
        orderSn, payAmount, orderId = order_modify
        productVoList = None # 押货单产品信息
        
        @allure.step("获取押货单信息")
        def step_mgmt_inventory_dis_mortgage_order_detail_id():
            
            nonlocal productVoList
            params = {"id": orderId}
            with _mgmt_inventory_dis_mortgage_order_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
            
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": orderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": productVoList["mortgageNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_order_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货单批量取消数据检查")
    def test_04_mgmt_dis_inventory_book_items(self, order_modify_2):
            
        orderSn, payAmount, orderId = order_modify_2
        productVoList = None # 押货单产品信息
        
        @allure.step("获取押货单信息")
        def step_mgmt_inventory_dis_mortgage_order_detail_id():
            
            nonlocal productVoList
            params = {"id": orderId}
            with _mgmt_inventory_dis_mortgage_order_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
            
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": orderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": productVoList["mortgageNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_order_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货单欠货不发数据检查")
    def test_05_mgmt_dis_inventory_book_items(self, order_stopDeliver):
            
        orderSn, returnOrderSn, payAmount = order_stopDeliver
        productVoList = None # 退货单产品信息
        id = None
        
        @allure.step("押货退货分页列表:获取id")
        def step_mgmt_inventory_dis_mortgage_returnOrder_listPage():
            
            nonlocal id
            params = deepcopy(self.params02) 
            params["orderSn"] = returnOrderSn               
            with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("押货退货单详情")
        def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
            
            nonlocal productVoList 
            params = {
                "id": id, 
            }              
            with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
            
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": returnOrderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": -productVoList["returnNum"], # 增减值
                    "bizType": 2, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 2 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_returnOrder_listPage()
        step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台押货退货数据检查")
    def test_06_mgmt_dis_inventory_book_items(self, mortgageReturn_85_DTYH):
            
        returnOrderSn = mortgageReturn_85_DTYH
        productVoList = None # 退货单产品信息
        id = None
        
        @allure.step("押货退货分页列表:获取id")
        def step_mgmt_inventory_dis_mortgage_returnOrder_listPage():
            
            nonlocal id
            params = deepcopy(self.params02) 
            params["orderSn"] = returnOrderSn               
            with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("押货退货单详情")
        def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
            
            nonlocal productVoList 
            params = {
                "id": id, 
            }              
            with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
            
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": returnOrderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": -productVoList["returnNum"], # 增减值
                    "bizType": 2, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 2 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_returnOrder_listPage()
        step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台套装组合数据检查")
    def test_07_mgmt_dis_inventory_book_items(self, inventory_combine):
            
        combine_detail = inventory_combine  
            
        @allure.step("查询实时库存台账明细:M7035")
        @stepreruns()    
        def step_01_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = combine_detail[1]["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": combine_detail[1]["orderNo"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": combine_detail[1]["adjustNum"], # 增减值
                    "bizType": 2, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 2 # 出入库：1入库 2出库
                }
        
        @allure.step("查询实时库存台账明细:M70355")
        @stepreruns()    
        def step_02_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = combine_detail[0]["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": combine_detail[0]["orderNo"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": combine_detail[0]["adjustNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        

        step_01_mgmt_dis_inventory_book_items()
        step_02_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台套装拆分数据检查")
    def test_08_mgmt_dis_inventory_book_items(self, inventory_split):
            
        split_detail = inventory_split 
            
        @allure.step("查询实时库存台账明细:M7035")    
        def step_01_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = split_detail[1]["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": split_detail[1]["orderNo"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": split_detail[1]["adjustNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        @allure.step("查询实时库存台账明细:M70355")    
        def step_02_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = split_detail[0]["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": split_detail[0]["orderNo"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": split_detail[0]["adjustNum"], # 增减值
                    "bizType": 2, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 2 # 出入库：1入库 2出库
                }
        

        step_01_mgmt_dis_inventory_book_items()
        step_02_mgmt_dis_inventory_book_items()


    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 完美运营后台13押货转移数据检查")
    def test_09_mgmt_dis_inventory_book_items(self, addTransfer):
            
        addTransferList, recordList = addTransfer # 库存列表:大于0的库存 
            
        @allure.step("查询实时库存台账明细")    
        def step_02_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = addTransferList["serialNo"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": recordList["orderSn"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": 1, # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_02_mgmt_dis_inventory_book_items()


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/book-items")
class TestClass02:
    """
    查询实时库存台账明细:店铺后台押货，押货退货，套装组合，13押货转移数据检查
    /mgmt/dis-inventory/book-items
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台押货单数据检查")
    def test_01_mgmt_dis_inventory_book_items(self, mortgageOrder_85_1):
            
        orderSn, payAmount = mortgageOrder_85_1
        productVoList = None # 押货单产品信息
        id = None
        
        @allure.step(" 押货单列表查询:获取id")
        def step_mgmt_inventory_dis_mortgage_order_listPage():
            
            nonlocal id
            params = deepcopy(self.params03)
            params["orderSn"] = orderSn               
            with _mgmt_inventory_dis_mortgage_order_listPage(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
        
        @allure.step("获取押货单信息")
        def step_mgmt_inventory_dis_mortgage_order_detail_id():
            
            nonlocal productVoList
            params = {"id": id}
            with _mgmt_inventory_dis_mortgage_order_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
                       
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": orderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": productVoList["mortgageNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_order_listPage()
        step_mgmt_inventory_dis_mortgage_order_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台押货退货数据检查")
    def test_02_mgmt_dis_inventory_book_items(self, mortgageReturn_85_TYH):
            
        returnOrderSn = mortgageReturn_85_TYH
        productVoList = None # 退货单产品信息
        id = None
        
        @allure.step("押货退货分页列表:获取id")
        def step_mgmt_inventory_dis_mortgage_returnOrder_listPage():
            
            nonlocal id
            params = deepcopy(self.params02) 
            params["orderSn"] = returnOrderSn               
            with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                id = r.json()["data"]["list"][0]["id"]
                
        @allure.step("押货退货单详情")
        def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
            
            nonlocal productVoList 
            params = {
                "id": id, 
            }              
            with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productVoList = r.json()["data"]["productList"][0]
            
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = productVoList["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": returnOrderSn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": -productVoList["returnNum"], # 增减值
                    "bizType": 2, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 2 # 出入库：1入库 2出库
                }
        
        step_mgmt_inventory_dis_mortgage_returnOrder_listPage()
        step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台套装组合数据检查")
    def test_03_mgmt_dis_inventory_book_items(self, inventory_combine_confirm):
            
        combine_detail = inventory_combine_confirm  
            
        @allure.step("查询实时库存台账明细:M7035")    
        def step_01_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = combine_detail["items"][1]["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": combine_detail["mortgageReturnCode"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": -combine_detail["items"][1]["diffNum"], # 增减值
                    "bizType": 2, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 2 # 出入库：1入库 2出库
                }
        
        @allure.step("查询实时库存台账明细:M70355")    
        def step_02_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = combine_detail["items"][0]["productCode"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": combine_detail["mortgageCode"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": combine_detail["items"][0]["diffNum"], # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_01_mgmt_dis_inventory_book_items()
        step_02_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 店铺后台13押货转移数据检查")
    def test_04_mgmt_dis_inventory_book_items(self, disInventoryTransfer_addTransfer):
            
        addTransferList, recordList = disInventoryTransfer_addTransfer # 库存列表:大于0的库存 
            
        @allure.step("查询实时库存台账明细")    
        def step_02_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = addTransferList["serialNo"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": recordList["orderSn"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": 1, # 增减值
                    "bizType": 1, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_02_mgmt_dis_inventory_book_items()



@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/book-items")
class TestClass03:
    """
    查询实时库存台账明细:商城转分订单，转分订单退款，转分结算前调整，转分结算前调整退款数据检查
    /mgmt/dis-inventory/book-items
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 商城转分订单数据检查")
    def test_01_mgmt_dis_inventory_book_items(self, orderCommit_85):
            
        getOrderInfo = orderCommit_85
                       
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = getOrderInfo["orderProductVOList"][0]["serialNo"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": getOrderInfo["orderNo"], # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": -getOrderInfo["orderProductVOList"][0]["quantity"], # 增减值
                    "bizType": 3, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 2 # 出入库：1入库 2出库
                }
        
        step_mgmt_dis_inventory_book_items()

    @allure.severity(P1)
    @allure.title("查询实时库存台账明细-成功路径: 商城转分订单退款数据检查")
    def test_02_mgmt_dis_inventory_book_items(self, applyReturn_85):
            
        applyReturn, getOrderInfo = applyReturn_85
            
        @allure.step("查询实时库存台账明细")    
        def step_mgmt_dis_inventory_book_items():
            
            params = deepcopy(self.params)
            params["storeCode"] = store_85            
            params["productCode"] = getOrderInfo["orderProductVOList"][0]["serialNo"]
            with _mgmt_dis_inventory_book_items(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"][0] == {
                    "bizNo": applyReturn, # 来源的 业务id （可能是押货id，可能是商城订单id）
                    "diffNum": getOrderInfo["orderProductVOList"][0]["quantity"], # 增减值
                    "bizType": 3, # 来源：1押货 2押货退货 3商城订单 4顾客退货 5库存调整 6补单 12押货调整
                    "type": 1 # 出入库：1入库 2出库
                }
        
        step_mgmt_dis_inventory_book_items()

