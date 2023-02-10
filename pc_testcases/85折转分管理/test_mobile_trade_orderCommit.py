# coding:utf-8

from api.mall_mobile_application._mobile_order_before_by_cardNo import params, _mobile_order_before_by_cardNo # 根据用户卡号查询是否可购买商品
from api.mall_mobile_application._mobile_product_discount_productList import data, _mobile_product_discount_productList # 查询85折转分商品
from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
from api.mall_mobile_application._mobile_product_discount_beforeSettlementProductList import data as data02, _mobile_product_discount_beforeSettlementProductList # 查询85折转分商品--结算前销售调整

from setting import P1, P2, P3, productCode, username_85, store_85

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/trade/orderCommit")
class TestClass:
    """
    提交订单
    /mobile/trade/orderCommit
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.token_85 = os.environ["token_85"]

    @allure.severity(P1)
    @allure.title("提交订单-成功路径: 85折转分订单检查")
    def test_mobile_trade_orderCommit(self):
        
        before_by_cardNo = None # 用户信息
        productList = None # 商品信息
        getFreightList = None # 运费补贴券
        getCouponList = None # 优惠券
        getSecondList = None # 秒返券
        getGiftList_2 = None # 电子礼券
        orderCommit = None # 订单信息
        number = 2 # 购买商品数量
        
        @allure.step("根据用户卡号查询是否可购买商品")
        def step_mobile_order_before_by_cardNo():
            
            nonlocal before_by_cardNo
            params = deepcopy(self.params) 
            params["cardNo"] = username_85
            with _mobile_order_before_by_cardNo(params, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                before_by_cardNo = r.json()["data"]
        
        @allure.step("查询85折转分商品")
        def step_mobile_product_discount_productList():
            
            nonlocal productList
            data = deepcopy(self.data)
            data["isSelected"] = 1
            data["selectedList"][0] = {"serialNo": "M7035","selectNums": 2}                    
            with _mobile_product_discount_productList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["serialNo"] == productCode:
                        productList = d

        @allure.step("获取运费补贴券列表")
        def step_mobile_order_carts_getFreightList():
            
            nonlocal getFreightList
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
            }         
            with _mobile_order_carts_getFreightList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getFreightList = r.json()["data"][0]

        @allure.step("获取选中结算分组的可用和不可用优惠券列表")
        def step_mobile_order_carts_getCouponList():
            
            nonlocal getCouponList
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "storeCode": store_85
            }         
            with _mobile_order_carts_getCouponList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["availableList"]:
                    getCouponList = r.json()["data"]["availableList"][0]

        @allure.step("获取购物秒返券券列表")
        def step_mobile_order_carts_getSecondList():
            
            nonlocal getSecondList
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "storeCode": store_85
            }        
            with _mobile_order_carts_getSecondList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    for d in r.json()["data"]:
                        if d["isUsed"] == 1:
                            getSecondList = d["secondCouponId"]

        @allure.step("获取电子礼券列表")
        def step_mobile_order_carts_getGiftList_2():
            
            nonlocal getGiftList_2
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
            }        
            with _mobile_order_carts_getGiftList_2(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getGiftList_2 = r.json()["data"][0]

        @allure.step("选择商品去结算")
        def step_mobile_order_carts_toSettlement():
            
            nonlocal getGiftList_2
            data = {
                "addressId": None,
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "customerId":  before_by_cardNo["id"], # 给某个顾客下单的会员ID
                "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "orderInvoice": None, # 发票信息
                "couponList": [], # 使用的优惠卷
                "giftList": [], # 使用的电子礼券
                "freightList": [], # 使用的运费补贴礼券
                "secondCouponList": [], # 使用的秒返券
                "storeCode": store_85, # 服务中心编码
                "ownerId": "", # 送货人ID
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0.12, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 8 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            }
            if getFreightList: # 运费补贴券
                data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
            if getCouponList: # 优惠卷
                data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
            if getSecondList: # 秒返券
                data["secondCouponList"].append({"secondCouponId": getSecondList})
            if getGiftList_2: # 电子礼券
                data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
            with _mobile_order_carts_toSettlement(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("提交订单")
        def step_mobile_trade_orderCommit():
            
            nonlocal orderCommit
            data = {
                "addressId": None,
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "customerId": before_by_cardNo["id"], # 给某个顾客下单的会员ID
                "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "orderInvoice": None, # # 发票信息
                "couponList": [], # 使用的优惠卷
                "giftList": [], # 使用的电子礼券
                "freightList": [], # 使用的运费补贴礼券
                "secondCouponList": [], # 使用的秒返券
                "storeCode": store_85, # 服务中心编码
                "ownerId": "", # 送货人ID
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0.12, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
                "isUpgrade": 0 # 是否升级单 0->否 1->是
            } 
            if getFreightList: # 运费补贴券
                data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
            if getCouponList: # 优惠卷
                data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
            if getSecondList: # 秒返券
                data["secondCouponList"].append({"secondCouponId": getSecondList})
            if getGiftList_2: # 电子礼券
                data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                    
            with _mobile_trade_orderCommit(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderCommit = r.json()["data"]

        step_mobile_order_before_by_cardNo()
        step_mobile_product_discount_productList()
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_mobile_order_carts_toSettlement()
        step_mobile_trade_orderCommit()

    @allure.severity(P1)
    @allure.title("提交订单-成功路径: 85折转分结算前调整订单检查")
    def test_mobile_trade_orderCommit(self):
        
        before_by_cardNo = None # 用户信息
        productList = None # 商品信息
        getFreightList = None # 运费补贴券
        getCouponList = None # 优惠券
        getSecondList = None # 秒返券
        getGiftList_2 = None # 电子礼券
        orderCommit = None # 订单信息
        number = 2 # 购买商品数量
        
        @allure.step("根据用户卡号查询是否可购买商品")
        def step_mobile_order_before_by_cardNo():
            
            nonlocal before_by_cardNo
            params = deepcopy(self.params) 
            params["cardNo"] = username_85
            with _mobile_order_before_by_cardNo(params, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                before_by_cardNo = r.json()["data"]
        
        @allure.step("查询85折转分商品")
        def step_mobile_product_discount_beforeSettlementProductList():
            
            nonlocal productList
            data = deepcopy(self.data)
            data["isSelected"] = 1
            data["selectedList"][0] = {"serialNo": "M7035","selectNums": 2}                    
            with _mobile_product_discount_beforeSettlementProductList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]["list"]:
                    if d["serialNo"] == productCode:
                        productList = d

        @allure.step("获取运费补贴券列表")
        def step_mobile_order_carts_getFreightList():
            
            nonlocal getFreightList
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
            }         
            with _mobile_order_carts_getFreightList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getFreightList = r.json()["data"][0]

        @allure.step("获取选中结算分组的可用和不可用优惠券列表")
        def step_mobile_order_carts_getCouponList():
            
            nonlocal getCouponList
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "storeCode": store_85
            }         
            with _mobile_order_carts_getCouponList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["availableList"]:
                    getCouponList = r.json()["data"]["availableList"][0]

        @allure.step("获取购物秒返券券列表")
        def step_mobile_order_carts_getSecondList():
            
            nonlocal getSecondList
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "storeCode": store_85
            }        
            with _mobile_order_carts_getSecondList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    for d in r.json()["data"]:
                        if d["isUsed"] == 1:
                            getSecondList = d["secondCouponId"]

        @allure.step("获取电子礼券列表")
        def step_mobile_order_carts_getGiftList_2():
            
            nonlocal getGiftList_2
            data = {
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "sourceType": 8,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": 2,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
            }        
            with _mobile_order_carts_getGiftList_2(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getGiftList_2 = r.json()["data"][0]

        @allure.step("选择商品去结算")
        def step_mobile_order_carts_toSettlement():
            
            nonlocal getGiftList_2
            data = {
                "addressId": None,
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "customerId":  before_by_cardNo["id"], # 给某个顾客下单的会员ID
                "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "orderInvoice": None, # 发票信息
                "couponList": [], # 使用的优惠卷
                "giftList": [], # 使用的电子礼券
                "freightList": [], # 使用的运费补贴礼券
                "secondCouponList": [], # 使用的秒返券
                "storeCode": store_85, # 服务中心编码
                "ownerId": "", # 送货人ID
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0.12, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 9 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            }
            if getFreightList: # 运费补贴券
                data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
            if getCouponList: # 优惠卷
                data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
            if getSecondList: # 秒返券
                data["secondCouponList"].append({"secondCouponId": getSecondList})
            if getGiftList_2: # 电子礼券
                data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
            with _mobile_order_carts_toSettlement(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("提交订单")
        def step_mobile_trade_orderCommit():
            
            nonlocal orderCommit
            data = {
                "addressId": None,
                "customerCard": username_85, # 给某个顾客下单的会员卡号
                "customerId": before_by_cardNo["id"], # 给某个顾客下单的会员ID
                "expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
                "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "orderInvoice": None, # # 发票信息
                "couponList": [], # 使用的优惠卷
                "giftList": [], # 使用的电子礼券
                "freightList": [], # 使用的运费补贴礼券
                "secondCouponList": [], # 使用的秒返券
                "storeCode": store_85, # 服务中心编码
                "ownerId": "", # 送货人ID
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0.12, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 9, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "commitType": 2, # 提交类型 null-普通提交(默认), 1-提交审核, 2-提交并完成
                "isUpgrade": 0 # 是否升级单 0->否 1->是
            } 
            if getFreightList: # 运费补贴券
                data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
            if getCouponList: # 优惠卷
                data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
            if getSecondList: # 秒返券
                data["secondCouponList"].append({"secondCouponId": getSecondList})
            if getGiftList_2: # 电子礼券
                data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})                    
            with _mobile_trade_orderCommit(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderCommit = r.json()["data"]

        step_mobile_order_before_by_cardNo()
        step_mobile_product_discount_beforeSettlementProductList()
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_mobile_order_carts_toSettlement()
        step_mobile_trade_orderCommit()

