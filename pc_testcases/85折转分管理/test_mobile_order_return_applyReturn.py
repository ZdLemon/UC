# coding:utf-8

from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data, _mobile_orderInfo_getClientOrderList # 85折订单列表
from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import params, _mobile_orderInfo_getOrderInfo # 85折订单信息
from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
from api.mall_mobile_application._mobile_web_order_return_getReturnType import params as params02, _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import params as params03, _mobile_web_order_as_returnMonthVerify # 隔月退货验证
from api.mall_mobile_application._mobile_web_order_as_upgradeOrderVerify import data as data02, _mobile_web_order_as_upgradeOrderVerify # 升级单校验
from api.mall_mobile_application._mobile_order_return_applyReturn import data as data03, _mobile_order_return_applyReturn # 申请退货/退款
from util.stepreruns import stepreruns
from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/order/return/applyReturn")
class TestClass:
    """
    申请退货/退款
    /mobile/order/return/applyReturn
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.data03 = deepcopy(data03)
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.token_85 = os.environ["token_85"]

    @allure.severity(P1)
    @allure.title("申请退货/退款-成功路径: 申请退货/退款检查")
    def test_mobile_order_return_applyReturn(self):
        
        getClientOrderList = None # 85折订单列表信息
        getReturnReasonByType = None # 退货/退款原因列表
        getReturnType = None # 获取退货类型：1：当月退 2：隔月退
        returnMonthVerify = None # 隔月退货验证结果
        upgradeOrderVerify = None # 升级单校验结果 结果类型 0->非升级单 1->可退升级单 2->存在其他PV订单 3->券已使用 4->非升级单产生的秒返券被用
        applyReturn = None # 退货单号
        
        @allure.step("85折订单列表,获取订单号")
        @stepreruns()
        def step_mobile_orderInfo_getClientOrderList():
            
            nonlocal getClientOrderList
            data = deepcopy(self.data)  
            data["orderStatus"] = [99] # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成 默认空为全部
            with _mobile_orderInfo_getClientOrderList(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getClientOrderList = r.json()["data"]["list"][0]
        
        @allure.step("查询85折订单信息")
        def step_mobile_orderInfo_getOrderInfo():
        
            params = deepcopy(self.params) 
            params["orderNo"] = getClientOrderList["orderNo"]
            with _mobile_orderInfo_getOrderInfo(params, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("退货/退款原因列表")
        def step_mobile_order_return_getReturnReasonByType():
            
            nonlocal getReturnReasonByType
            with _mobile_order_return_getReturnReasonByType(self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getReturnReasonByType = r.json()["data"]

        @allure.step("获取退货类型")
        def step_mobile_web_order_return_getReturnType():
            
            nonlocal getReturnType
            params = deepcopy(self.params02) 
            with _mobile_web_order_return_getReturnType(params, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                getReturnType = r.json()["data"]
        
        @allure.step("隔月退货验证")
        def step_mobile_web_order_as_returnMonthVerify():
            
            nonlocal returnMonthVerify
            params = deepcopy(self.params03) 
            params["orderNo"] = getClientOrderList["orderNo"]
            with _mobile_web_order_as_returnMonthVerify(params, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                returnMonthVerify = r.json()["data"]

        @allure.step("升级单校验")
        def step_mobile_web_order_as_upgradeOrderVerify():
            
            nonlocal upgradeOrderVerify
            data = deepcopy(self.data02) 
            data["orderNo"] = getClientOrderList["orderNo"]
            with _mobile_web_order_as_upgradeOrderVerify(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                upgradeOrderVerify = r.json()["data"]["resultType"]      

        @allure.step("申请退货/退款")
        def step_mobile_order_return_applyReturn():
            
            nonlocal applyReturn
            data = deepcopy(self.data03) 
            data["orderNo"] = getClientOrderList["orderNo"]
            data["reason1"] = getReturnReasonByType[0]["returnReason"]
            data["reason1Id"] = getReturnReasonByType[0]["id"]
            with _mobile_order_return_applyReturn(data, self.token_85) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                applyReturn = r.json()["data"]
    
          
        step_mobile_orderInfo_getClientOrderList()
        step_mobile_orderInfo_getOrderInfo()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_returnMonthVerify()
        step_mobile_web_order_as_upgradeOrderVerify()
        step_mobile_order_return_applyReturn()
