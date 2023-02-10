# coding:utf-8

from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data, _mobile_orderInfo_getClientOrderList # 85折订单列表
from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import params, _mobile_orderInfo_getOrderInfo # 85折订单信息
from api.mall_mobile_application._mobile_order_return_getReturnReasonByType import _mobile_order_return_getReturnReasonByType # 退货/退款原因列表
from api.mall_mobile_application._mobile_web_order_return_getReturnType import params as params02, _mobile_web_order_return_getReturnType # 获取退货类型：1：当月退 2：隔月退
from api.mall_mobile_application._mobile_web_order_as_returnMonthVerify import params as params03, _mobile_web_order_as_returnMonthVerify # 隔月退货验证
from util.stepreruns import stepreruns
from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/web/order/as/returnMonthVerify")
class TestClass:
    """
    隔月退货验证
    /mobile/web/order/as/returnMonthVerify
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.params02 = deepcopy(params02)
        self.params03 = deepcopy(params03)
        self.token_85 = os.environ["token_85"]

    @allure.severity(P1)
    @allure.title("隔月退货验证-成功路径: 85折转分订单退货时隔月退货验证检查")
    def test_mobile_web_order_as_returnMonthVerify(self):
        
        getClientOrderList = None # 85折订单列表信息
        getReturnReasonByType = None # 退货/退款原因列表
        getReturnType = None # 获取退货类型：1：当月退 2：隔月退
        returnMonthVerify = "" # 隔月退货验证结果
        
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
        
        
        step_mobile_orderInfo_getClientOrderList()
        step_mobile_orderInfo_getOrderInfo()
        step_mobile_order_return_getReturnReasonByType()
        step_mobile_web_order_return_getReturnType()
        step_mobile_web_order_as_returnMonthVerify()
