# coding:utf-8

from api.mall_mobile_application._mobile_product_search import data, _mobile_product_search # 搜索商品
from api.mall_mobile_application._mobile_personalInfo_getCurrentUserInfo import _mobile_personalInfo_getCurrentUserInfo # 个人用户信息接口
from api.mall_mobile_application._mobile_personalInfo_getMemberAddressList import _mobile_personalInfo_getMemberAddressList # 获取当前登录用户的配送地址列表接口
from api.mall_mobile_application._mobile_order_carts_getFreightList import _mobile_order_carts_getFreightList # 获取运费补贴券券列表
from api.mall_mobile_application._mobile_order_carts_getCouponList import _mobile_order_carts_getCouponList # 获取选中结算分组的可用和不可用优惠券列表
from api.mall_mobile_application._mobile_order_carts_getSecondList import _mobile_order_carts_getSecondList # 获取购物秒返券券列表
from api.mall_mobile_application._mobile_order_carts_getGiftList_2 import _mobile_order_carts_getGiftList_2 # 获取电子礼券列表
from api.mall_mobile_application._mobile_order_carts_toSettlement import _mobile_order_carts_toSettlement # 选择商品去结算
from api.mall_mobile_application._mobile_trade_orderCommit import _mobile_trade_orderCommit # 提交订单
from api.mall_mobile_application._mobile_wallet_queryPasswordExist import _mobile_wallet_queryPasswordExist # 是否设置了支付密码
from api.mall_mobile_application._mobile_wallet_getDetail import _mobile_wallet_getDetail # 获取钱包首页相关信息
from api.mall_mobile_application._mobile_payment_getPayMethod import _mobile_payment_getPayMethod #  获取支付方式
from api.mall_center_pay._pay_notify_mockPaySuccess import _pay_notify_mockPaySuccess # 银联支付回调
from api.mall_mobile_application._mobile_payment_singlePay import _mobile_payment_singlePay # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
from api.mall_mobile_application._mobile_payment_queryWalletPayOrder import _mobile_payment_queryWalletPayOrder # 查询支付成功信息
from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import _mobile_orderInfo_getOrderInfo # 通过订单号查询客户端订单信息

from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall-mobile-application")
@allure.story("/mobile/payment/associationPay")
class TestClass:
    """
    组合支付,【适用于云商,微店（云+）,云商/微店的子账号,店员】 当钱包可用余额足够支付,二选一，钱包支付或者第三方支付；
    当钱包可用余额不足以支付，选择钱包+第三方。店员需具备支付权限
    /mobile/payment/associationPay
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.token = os.environ["pk_token"]

    
    @allure.severity(P1)
    @allure.title("组合支付-成功路径: 云商自购下单-钱包支付检查")
    @pytest.mark.skip()
    def test_mobile_payment_associationPay(self, login_oauth_token):
              
        productList = None # 商品详情
        getFreightList = None # 运费补贴券
        getCouponList = None # 优惠券
        getSecondList = None # 秒返券
        getGiftList_2 = None # 电子礼券
        availableBalance = None # 钱包可用余额
        associationPay = None # 支付方式-邮政储蓄银行信息
        orderCommit = None # 订单信息
        payOrderNo = None # 支付流水号
        queryWalletPayOrder = None # 支付成功信息
        getOrderInfo = None # 详细订单信息
        number = 2 # 购买商品数量
        user = login_oauth_token["data"] # 给某个顾客下单的信息（非下单人）
        
        @allure.step("搜索商品")
        def step_mobile_product_search():

            nonlocal productList
            data = deepcopy(self.data)
            data["keyword"] = productCode
            with _mobile_product_search(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productList = r.json()["data"]["list"][0]

        @allure.step("获取运费补贴券列表")
        def step_mobile_order_carts_getFreightList():
            
            nonlocal getFreightList
            data = {
                "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
            }         
            with _mobile_order_carts_getFreightList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getFreightList = r.json()["data"][0]

        @allure.step("获取选中结算分组的可用和不可用优惠券列表")
        def step_mobile_order_carts_getCouponList():
                        
            nonlocal getCouponList
            data = {
                "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "storeCode": user["storeCode"]
            }         
            with _mobile_order_carts_getCouponList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["availableList"]:
                    getCouponList = r.json()["data"]["availableList"][0]

        @allure.step("获取购物秒返券券列表")
        def step_mobile_order_carts_getSecondList():
                        
            nonlocal getSecondList
            data = {
                "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
                "storeCode": user["storeCode"]
            }        
            with _mobile_order_carts_getSecondList(data, self.token) as r:            
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
                "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "serialNo": productList["serialNo"],
                    "number": number,
                    "retailPrice": productList["retailPrice"],
                    "pv": productList["pv"],
                    "imgUrl": productList["imgUrl"],
                    "title": productList["title"]
                }],
            }        
            with _mobile_order_carts_getGiftList_2(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getGiftList_2 = r.json()["data"][0]

        @allure.step("选择商品去结算")
        def step_mobile_order_carts_toSettlement():
                        
            data = {
                "addressId": None,
                "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                "customerId":  user["userId"], # 给某个顾客下单的会员ID
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
                "storeCode": user["storeCode"], # 服务中心编码
                "ownerId": "", # 送货人ID
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0.12, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 0 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            }
            if getFreightList: # 运费补贴券
                data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
            if getCouponList: # 优惠卷
                data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
            if getSecondList: # 秒返券
                data["secondCouponList"].append({"secondCouponId": getSecondList})
            if getGiftList_2: # 电子礼券
                data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
            with _mobile_order_carts_toSettlement(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("提交订单")
        def step_mobile_trade_orderCommit():
                        
            nonlocal orderCommit
            data = {
                "addressId": None,
                "customerCard": user["cardNo"], # 给某个顾客下单的会员卡号
                "customerId": user["userId"], # 给某个顾客下单的会员ID
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
                "storeCode": user["storeCode"], # 服务中心编码
                "ownerId": "", # 送货人ID
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0.12, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
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
            with _mobile_trade_orderCommit(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderCommit = r.json()["data"]

        @allure.step("是否设置了支付密码")
        def step_mobile_wallet_queryPasswordExist():
            
            with _mobile_wallet_queryPasswordExist(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
         
        @allure.step("获取钱包首页相关信息")
        def step_mobile_wallet_getDetail():
            
            nonlocal  availableBalance
            with _mobile_wallet_getDetail(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                availableBalance = r.json()["data"]["availableBalance"]
        
        @allure.step("获取支付方式")
        def step_mobile_payment_getPayMethod():

            nonlocal associationPay
            data = {
                "orderNoList":[orderCommit["orderNo"]], # 订单号集合
                "payType":"PC", # 支付类型,H5、APP、PC、PROGRAM
                "sourceType":1 # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整) 结算前销售调整sourceType不能为空
            }
            with _mobile_payment_getPayMethod(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for d in r.json()["data"]:
                    if d["bankName"] == "邮政储蓄银行":
                        associationPay = d

        @allure.step("支付")
        def step_mobile_payment_associationPay():

            nonlocal payOrderNo
            data = {
                "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=(应付金额-钱包可用余额)*费率+应付金额
                "channelCode": 800, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
                "orderNoList": [orderCommit["orderNo"]],
                "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
                "payableAmt": orderCommit["totalAmount"], # 订单总应付金额
                "feeRate": 0, # 手续费率
                "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false",
                "walletPassword": "", # 钱包充值密码,非免密必传字段
                "orderNo": orderCommit["orderNo"]
            }
            with _mobile_payment_associationPay(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                payOrderNo = r.json()["data"]["payOrderNo"]

        @allure.step("查询支付成功信息")
        def step_mobile_payment_queryWalletPayOrder():

            nonlocal queryWalletPayOrder
            params = {
                "payNo": payOrderNo, # 订单编号(必填)
            }
            with _mobile_payment_queryWalletPayOrder(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                queryWalletPayOrder = r.json()["data"]

        @allure.step("通过订单号查询客户端订单信息")
        def step_mobile_orderInfo_getOrderInfo():

            nonlocal getOrderInfo
            params = {
                "orderNo": orderCommit["orderNo"] # 订单编号(必填)
            }
            with _mobile_orderInfo_getOrderInfo(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderInfo = r.json()["data"]
               
        step_mobile_product_search()
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_mobile_order_carts_toSettlement()
        step_mobile_trade_orderCommit()
        step_mobile_wallet_queryPasswordExist()
        step_mobile_wallet_getDetail()
        step_mobile_payment_getPayMethod()
        step_mobile_payment_associationPay()
        step_mobile_payment_queryWalletPayOrder()
        step_mobile_orderInfo_getOrderInfo()
        
        return queryWalletPayOrder, getOrderInfo
        
    @allure.severity(P1)
    @allure.title("普客-公司配送-银联支付检查")
    def test_02_mobile_payment_associationPay(self):
              
        productList = None # 商品详情
        getCurrentUserInfo = None # 个人用户信息
        getMemberAddressList = None # 获取当前登录用户的配送地址列表
        singlePay = None # 单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付
        getFreightList = None # 运费补贴券
        getCouponList = None # 优惠券
        getSecondList = None # 秒返券
        getGiftList_2 = None # 电子礼券
        orderCommit = None # 订单信息
        getOrderInfo = None # 详细订单信息
        number = 1 # 购买商品数量
        
        @allure.step("搜索商品")
        def step_mobile_product_search():

            nonlocal productList
            data = deepcopy(self.data)
            data["keyword"] = productCode
            with _mobile_product_search(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                productList = r.json()["data"]["list"][0]

        @allure.step("个人用户信息")
        def step_mobile_personalInfo_getCurrentUserInfo():

            nonlocal getCurrentUserInfo
            with _mobile_personalInfo_getCurrentUserInfo(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getCurrentUserInfo = r.json()["data"]

        @allure.step("获取当前登录用户的配送地址列表")
        def step_mobile_personalInfo_getMemberAddressList():

            nonlocal getMemberAddressList
            with _mobile_personalInfo_getMemberAddressList(self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getMemberAddressList = r.json()["data"]

        @allure.step("获取运费补贴券列表")
        def step_mobile_order_carts_getFreightList():
            
            nonlocal getFreightList
            data = {
                "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "activityPrice": productList["retailPrice"],
                    "imgUrl": productList["imgUrl"],
                    "isActivateItem": productList["isActivateItem"],
                    "isActivity": "",
                    "number": number,
                    "productType": productList["productType"],
                    "pv": productList["pv"],
                    "quantity": 1,
                    "releList": [],
                    "retailPrice": productList["retailPrice"],
                    "serialNo": productList["serialNo"],
                    "title": productList["title"]
                }],
            }         
            with _mobile_order_carts_getFreightList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getFreightList = r.json()["data"][0]

        @allure.step("获取选中结算分组的可用和不可用优惠券列表")
        def step_mobile_order_carts_getCouponList():
                        
            nonlocal getCouponList
            data = {
                "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "activityPrice": productList["retailPrice"],
                    "imgUrl": productList["imgUrl"],
                    "isActivateItem": productList["isActivateItem"],
                    "isActivity": "",
                    "number": number,
                    "productType": productList["productType"],
                    "pv": productList["pv"],
                    "quantity": 1,
                    "releList": [],
                    "retailPrice": productList["retailPrice"],
                    "serialNo": productList["serialNo"],
                    "title": productList["title"]
                }]
            }         
            with _mobile_order_carts_getCouponList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]["availableList"]:
                    getCouponList = r.json()["data"]["availableList"][0]

        @allure.step("获取购物秒返券券列表")
        def step_mobile_order_carts_getSecondList():
                        
            nonlocal getSecondList
            data = {
                "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "activityPrice": productList["retailPrice"],
                    "imgUrl": productList["imgUrl"],
                    "isActivateItem": productList["isActivateItem"],
                    "isActivity": "",
                    "number": number,
                    "productType": productList["productType"],
                    "pv": productList["pv"],
                    "quantity": 1,
                    "releList": [],
                    "retailPrice": productList["retailPrice"],
                    "serialNo": productList["serialNo"],
                    "title": productList["title"]
                }]
            }        
            with _mobile_order_carts_getSecondList(data, self.token) as r:            
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
                "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
                "sourceType": 0,  # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
                "productList": [{
                    "activityPrice": productList["retailPrice"],
                    "imgUrl": productList["imgUrl"],
                    "isActivateItem": productList["isActivateItem"],
                    "isActivity": "",
                    "number": number,
                    "productType": productList["productType"],
                    "pv": productList["pv"],
                    "quantity": 1,
                    "releList": [],
                    "retailPrice": productList["retailPrice"],
                    "serialNo": productList["serialNo"],
                    "title": productList["title"]
                }]
            }        
            with _mobile_order_carts_getGiftList_2(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                if r.json()["data"]:
                    getGiftList_2 = r.json()["data"][0]

        @allure.step("选择商品去结算")
        def step_mobile_order_carts_toSettlement():
                        
            data = {
                "addressId": getMemberAddressList[0]["id"],
                "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
                "customerId":  getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
                "expressType": 2, # 配送方式 1->服务中心自提 2->公司配送
                "orderAmount": productList["retailPrice"] * number, # 商品金额,提交订单时必传(零售价*数量)
                "productList": [{
                    "activityPrice": productList["retailPrice"],
                    "imgUrl": productList["imgUrl"],
                    "isActivateItem": productList["isActivateItem"],
                    "isActivity": "",
                    "number": number,
                    "productType": productList["productType"],
                    "pv": productList["pv"],
                    "quantity": 1,
                    "releList": [],
                    "retailPrice": productList["retailPrice"],
                    "serialNo": productList["serialNo"],
                    "title": productList["title"]
                }],
                "orderInvoice": None, # 发票信息
                "couponList": [], # 使用的优惠卷
                "giftList": [], # 使用的电子礼券
                "freightList": [], # 使用的运费补贴礼券
                "secondCouponList": [], # 使用的秒返券
                "storeCode": None, # 服务中心编码
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 0 # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
            }
            if getFreightList: # 运费补贴券
                data["freightList"].append({"grantdtlId": getFreightList["grantdtlId"]})
            if getCouponList: # 优惠卷
                data["couponList"].append({"memberCouponId": getCouponList["couponMemberId"],"couponType": getCouponList["couponType"],"cartCouponAmount": getCouponList["cartCouponAmount"]})
            if getSecondList: # 秒返券
                data["secondCouponList"].append({"secondCouponId": getSecondList})
            if getGiftList_2: # 电子礼券
                data["giftList"].append({"grantdtlId": getGiftList_2["grantdtlId"]})        
            with _mobile_order_carts_toSettlement(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200

        @allure.step("提交订单")
        def step_mobile_trade_orderCommit():
                        
            nonlocal orderCommit
            data = {
                "addressId": getMemberAddressList[0]["id"],
                "customerCard": getCurrentUserInfo["cardNo"], # 给某个顾客下单的会员卡号
                "customerId": getCurrentUserInfo["id"], # 给某个顾客下单的会员ID
                "expressType": 2, # 配送方式 1->服务中心自提 2->公司配送
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
                "storeCode": None, # 服务中心编码
                "ownerId": "", # 送货人ID
                "pv": productList["pv"] * number,
                "remarks": "", # 备注
                "returnRate": 0, # 返还比例
                "sharerId": None, # 分享人id
                "sourceType": 0, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
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
            with _mobile_trade_orderCommit(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderCommit = r.json()["data"]

        @allure.step("单一支付,【适用所有顾客】 要么钱包单独付款、要么第三方单独支付")
        def step_mobile_payment_singlePay():
            
            nonlocal singlePay
            data = {
                "actualAmt": orderCommit["totalAmount"], # 实付金额 税率为零时等于应付金额,不为零时,实付金额=订单应付金额+订单应付金额*费率信息
                "channelCode": 103, # 支付渠道 支付方式 101：微信；102：支付宝；103：银联；201:工商银行 202：建设银行 204：交通银行 800:钱包支付
                "orderNoList": [orderCommit["orderNo"]],
                "payType": "PC", # 支付类型,H5、APP、PC、PROGRAM
                "payableAmt": orderCommit["totalAmount"], # 订单应付金额
                "feeRate": 0, # 手续费率
                "jumpUrl": "https://uc-test.perfect99.com/personalCenter/myOrder?isUpgrade=false", # 支付成功前端跳转地址,微信支付必传字段信息
                "walletPassword": "" # 钱包密码,非免密必传字段
            }   
            with _mobile_payment_singlePay(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                singlePay = r.json()["data"]
         
        @allure.step("银联支付回调")
        def step_pay_notify_mockPaySuccess():

            params = {
                "payOrderNo": singlePay["payOrderNo"],
            }
            with _pay_notify_mockPaySuccess(params, self.token) as r:            
                assert r.status_code == 200
                assert r.text == "SUCCESS"

        @allure.step("通过订单号查询客户端订单信息")
        def step_mobile_orderInfo_getOrderInfo():

            nonlocal getOrderInfo
            params = {
                "orderNo": orderCommit["orderNo"] # 订单编号(必填)
            }
            with _mobile_orderInfo_getOrderInfo(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getOrderInfo = r.json()["data"]
               
        step_mobile_product_search()
        step_mobile_personalInfo_getCurrentUserInfo()
        step_mobile_personalInfo_getMemberAddressList()
        step_mobile_order_carts_getFreightList()
        step_mobile_order_carts_getCouponList()
        step_mobile_order_carts_getSecondList()
        step_mobile_order_carts_getGiftList_2()
        step_mobile_order_carts_toSettlement()
        step_mobile_trade_orderCommit()
        step_mobile_payment_singlePay()
        step_pay_notify_mockPaySuccess()
        step_mobile_orderInfo_getOrderInfo()
        
        return getOrderInfo
        
         
            


