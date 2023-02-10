# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getReason import params, _mgmt_inventory_common_getReason # 退换货原因
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_searchStore import params as params02, _mgmt_inventory_dis_mortgage_common_searchStore # 查询店铺信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_searchProduct import params as params03, _mgmt_inventory_dis_mortgage_returnOrder_searchProduct # 获取商品信息
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn import _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn # 新建押货退货单
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_listPage import params as params04, _mgmt_inventory_dis_mortgage_returnOrder_listPage # 押货退货列表
from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_returnOrder_detail_id import params as params05, _mgmt_inventory_dis_mortgage_returnOrder_detail_id # 押货退货单详情

from util.stepreruns import stepreruns
from setting import P1, P2, P3, store_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/returnOrder/detail/")
class TestClass:
    """
    押货退详情
    /mgmt/inventory/dis/mortgage/returnOrder/detail/{id}
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.params04 = deepcopy(params04)
        self.params05 = deepcopy(params05)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P1)
    @allure.title("押货退详情-成功路径: 押货退详情检查")
    def test_mgmt_inventory_dis_mortgage_returnOrder_detail_id(self):
        
        getReason = None # 退换货原因
        searchStore = None # 店铺信息
        searchProduct = None # 商品信息
        id = None # 押货退货单id
        listPage = None # 押货退货列表信息
        
        @allure.step("获取各种退换货原因")
        def test_mgmt_inventory_common_getReason():
            
            nonlocal getReason
            params = deepcopy(self.params)
            params["type:"] = 3 # 退货原因              
            with _mgmt_inventory_common_getReason(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]
        
        @allure.step("查询店铺信息")
        def test_mgmt_inventory_dis_mortgage_common_searchStore():
            
            nonlocal searchStore
            params = deepcopy(self.params02)
            params["storeCode"] = store_85                   
            with _mgmt_inventory_dis_mortgage_common_searchStore(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchStore = r.json()["data"]
        
        @allure.step("商品编码搜索退货商品信息")
        def step_mgmt_inventory_dis_mortgage_returnOrder_searchProduct():
            
            nonlocal searchProduct
            params = deepcopy(self.params03) 
            params["storeCode"] = store_85
            params["productCode"] = productCode           
            with _mgmt_inventory_dis_mortgage_returnOrder_searchProduct(params, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                searchProduct = r.json()["data"]
        
        @allure.step("新建85折押货退货单")
        def step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn():
            
            nonlocal id
            data = {
                "productList": [{
                    "productCode": searchProduct["productCode"], # 商品编号
                    "productName": searchProduct["productName"], # 商品名称
                    "packing": searchProduct["packing"],
                    "unit": searchProduct["unit"],
                    "pieceBoxNorm": None,
                    "pieceBoxPrice": None,
                    "mortgagePrice": searchProduct["mortgagePrice"], # 85折押货价
                    "retailPrice": searchProduct["retailPrice"], # 零售价
                    "inventoryNum": searchProduct["inventoryNum"], # 库存数量
                    "returnNum": 2, # 退货数量
                    "remark": ""
                }],
                "orderMark": 0,
                "reasonFirst": getReason[1]["returnReason"],
                "reasonFirstRemark": "",
                "reasonSecond": getReason[1]["reasonList"][1]["returnReason"],
                "reasonSecondRemark": "",
                "storeCode": searchStore["storeCode"]
            }               
            with _mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn(data, self.access_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                id = r.json()["data"]

        @allure.step("押货退货分页列表:获取id")
        @stepreruns()
        def step_mgmt_inventory_dis_mortgage_returnOrder_listPage():
            
            nonlocal listPage
            params = deepcopy(self.params04) 
            params["storeCode"] = store_85               
            with _mgmt_inventory_dis_mortgage_returnOrder_listPage(params, self.access_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["id"] == id:
                        listPage = d
                        break

        @allure.step("押货退货单详情")
        def step_mgmt_inventory_dis_mortgage_returnOrder_detail_id():
            
            params = deepcopy(self.params05) 
            params["id"] = id              
            with _mgmt_inventory_dis_mortgage_returnOrder_detail_id(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["id"] == id
                assert r.json()["data"]["orderSn"] == listPage["orderSn"]

        test_mgmt_inventory_common_getReason()
        test_mgmt_inventory_dis_mortgage_common_searchStore()
        step_mgmt_inventory_dis_mortgage_returnOrder_searchProduct()
        step_mgmt_inventory_dis_mortgage_returnOrder_mortgageReturn()
        step_mgmt_inventory_dis_mortgage_returnOrder_listPage()
        step_mgmt_inventory_dis_mortgage_returnOrder_detail_id()
