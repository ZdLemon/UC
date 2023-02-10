# coding:utf-8

from api.mall_store_application._appStore_store_dis_mortgageOrder_searchProductPage import params, _appStore_store_dis_mortgageOrder_searchProductPage
from api.mall_store_application._appStore_store_dis_mortgageOrder_pushProductsToCart import data, _appStore_store_dis_mortgageOrder_pushProductsToCart
from api.mall_store_application._appStore_store_dis_mortgageOrder_mortgage import data as data02, _appStore_store_dis_mortgageOrder_mortgage
from api.mall_store_application._appStore_store_dis_mortgageOrder_prePayCheck import data as data03, _appStore_store_dis_mortgageOrder_prePayCheck
from api.mall_store_application._appStore_store_dis_mortgageOrder_detail_id import params as params02, _appStore_store_dis_mortgageOrder_detail_id
from api.mall_store_application._appStore_api_wallet_pay import _appStore_api_wallet_pay
from api.mall_store_application._appStore_store_deposit_msg import params as params03, _appStore_store_deposit_msg
from setting import P1, P2, P3, username_85, store_85, name_85, productCode

from copy import deepcopy
import os
import allure
import uuid


@allure.feature("mall_store_application")
@allure.story("/appStore/api/wallet/pay")
class TestClass:
    """
    支付
    /appStore/api/wallet/pay
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P1)
    @allure.title("支付-成功路径:押货单支付检查")
    def test_appStore_api_wallet_pay(self, login_store):
        
        searchProductPage = None # 商品信息
        id = None # 押货单id
        payAmount = None # 押货单金额
        balance = None # 保证金余额
        
        
        @allure.step("关键字搜索可押货商品分页,获取商品信息")
        def step_appStore_store_dis_mortgageOrder_searchProductPage():
            
            nonlocal searchProductPage
            params = deepcopy(self.params) 
            params["keyword"] = productCode
            with _appStore_store_dis_mortgageOrder_searchProductPage(params, self.store_token) as r:
                for d in r.json()["data"]["list"]:
                    if d["productCode"] == productCode:
                        searchProductPage = d
                        break  
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("推送购物车数据")
        def step_appStore_store_dis_mortgageOrder_pushProductsToCart():
            
            data = deepcopy(self.data) 
            data[0]["mortgageNum"] = 2
            data[0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data[0]["productCode"] = searchProductPage["productCode"]
            with _appStore_store_dis_mortgageOrder_pushProductsToCart(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货下单, 获取押货单Id")
        def step_appStore_store_dis_mortgageOrder_mortgage():
            
            nonlocal id
            data = deepcopy(self.data02)
            data["productList"][0]["mortgageNum"] = 2
            data["productList"][0]["mortgagePrice"] = searchProductPage["mortgagePrice"]
            data["productList"][0]["productCode"] = searchProductPage["productCode"]
            data["storeCode"]= store_85
            data["transId"]= f"KEY_{store_85}_{uuid.uuid1()}" # 业务id
            with _appStore_store_dis_mortgageOrder_mortgage(data, self.store_token) as r:
                id = r.json()["data"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("押货单详情, 获取押货单金额")
        def step_appStore_store_dis_mortgageOrder_detail_id():
            
            nonlocal payAmount
            params = deepcopy(self.params02)
            params["id"] = id
            with _appStore_store_dis_mortgageOrder_detail_id(params, self.store_token) as r:
                payAmount = r.json()["data"]["payAmount"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200

        @allure.step("获取服务中心可用押货保证金余额")
        def step_appStore_store_deposit_msg():
            
            nonlocal balance
            params = deepcopy(self.params03)
            params["storeCode"] = store_85
            with _appStore_store_deposit_msg(params, self.store_token) as r:
                balance = r.json()["data"]["balance"]
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                  
        @allure.step("押货单支付前的金额校验")
        def step_appStore_store_dis_mortgageOrder_prePayCheck():
            
            data = deepcopy(self.data03)
            data["orderId"] = id
            data["oweDepositAmount"] = 0
            data["payAmount"] = payAmount
            with _appStore_store_dis_mortgageOrder_prePayCheck(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
        
        @allure.step("押货单支付")
        def step_appStore_api_wallet_pay():
            
            data = {
                "accountName": "", # 户名(仅钱包支付不用传)
                "bankAccount": "", # 代扣账户(仅钱包支付不用传)
                "bankName": "", # 开户银行名称(仅钱包支付不用传)
                "businessType": 2, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "depositAmount": balance, # 支付时保证金余额(钱包、组合支付时必传,仅代扣不用传)
                "extJson": str({"balance":balance,"payAmount":payAmount,"payWays":[{"name":"押货保证金支付","payAmount":payAmount,"data":None}]}), # 扩展参数
                "payAmount": payAmount,
                "payChannel": "WEB", # 支付渠道 WEB/APP
                "payType": 1, # 支付方式 1-> 保证金 2->工行签约代扣 3->建行签约代扣 4->工行代扣、保证金组合支付, 5->建行代扣、保证金组合支付
                "storeCode": store_85, # 店铺编号
                "uniqueFlagNo": id, # 订单唯一标识
                "userId": login_store["data"]["userId"] # 用户ID
            }
            with _appStore_api_wallet_pay(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["data"]["payStatus"] == 2
        
        step_appStore_store_dis_mortgageOrder_searchProductPage()
        step_appStore_store_dis_mortgageOrder_pushProductsToCart()
        step_appStore_store_dis_mortgageOrder_mortgage()
        step_appStore_store_dis_mortgageOrder_detail_id()
        step_appStore_store_deposit_msg()
        step_appStore_store_dis_mortgageOrder_prePayCheck()
        step_appStore_api_wallet_pay()

