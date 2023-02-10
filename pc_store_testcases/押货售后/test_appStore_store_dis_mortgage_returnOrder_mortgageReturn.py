# coding:utf-8

from api.mall_store_application._appStore_common_getReason import params, _appStore_common_getReason # 获取各种退换货原因
from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_searchPositiveProducts import params as params02, _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts # 获取服务中心正库存的商品信息
from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_mortgageReturn import _appStore_store_dis_mortgage_returnOrder_mortgageReturn # 押货退货下单
from api.mall_store_application._appStore_store_dis_mortgage_returnOrder_listPage import params as params03, _appStore_store_dis_mortgage_returnOrder_listPage # 押货退货分页列表
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/store/dis/mortgage/returnOrder/mortgageReturn")
class TestClass:
    """
    押货退货下单
    /appStore/store/dis/mortgage/returnOrder/mortgageReturn
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.store_token_85 = os.environ["store_token_85"]
               
    @allure.severity(P1)
    @allure.title("押货退货下单-成功路径:85折押货退货下单检查")
    def test_appStore_store_dis_mortgage_returnOrder_mortgageReturn(self):
        
        returnNum = 2 # 退货数量
        getReason = None # 获取各种退换货原因
        searchPositiveProducts = None # 正库存商品编号
        mortgageReturn = None # 押货退货单id
        orderSn = None # 押货退货单号
        
        @allure.step("获取各种退换货原因")
        def step_appStore_common_getReason():
            
            nonlocal getReason
            params = deepcopy(self.params)
            with _appStore_common_getReason(params, self.store_token_85) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getReason = r.json()["data"]
            
        @allure.step("获取服务中心正库存的商品信息")
        def step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts():
            
            nonlocal searchPositiveProducts
            params = deepcopy(self.params02)
            with _appStore_store_dis_mortgage_returnOrder_searchPositiveProducts(params, self.store_token_85) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["productCode"] == productCode:
                        searchPositiveProducts = d["productCode"]
        
        @allure.step("押货退货下单")
        def step_appStore_store_dis_mortgage_returnOrder_mortgageReturn():
            
            nonlocal mortgageReturn
            data = {
                "reasonFirst": getReason[1]["returnReason"], # 一级原因
                "reasonFirstRemark": "", # 一级原因备注
                "productList": [{
                    "productCode": searchPositiveProducts, # 商品编码
                    "productNum": returnNum,
                    "productRemarks": "",
                    "remark": "", # 商品备注
                    "returnNum": returnNum # 商品退货数量
                }], 
                "storeCode": store_85 # 服务中心编码
            }
            with _appStore_store_dis_mortgage_returnOrder_mortgageReturn(data, self.store_token_85) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                mortgageReturn = r.json()["data"]
                
        @allure.step("押货退货分页列表:获取押货退货单号")
        def step_appStore_store_dis_mortgage_returnOrder_listPage():
            
            nonlocal orderSn
            params = deepcopy(self.params03)
            with _appStore_store_dis_mortgage_returnOrder_listPage(params, self.store_token_85) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["id"] == mortgageReturn:
                        orderSn = d["orderSn"]
                        
        step_appStore_common_getReason()
        step_appStore_store_dis_mortgage_returnOrder_searchPositiveProducts()
        step_appStore_store_dis_mortgage_returnOrder_mortgageReturn()
        step_appStore_store_dis_mortgage_returnOrder_listPage()
                    



