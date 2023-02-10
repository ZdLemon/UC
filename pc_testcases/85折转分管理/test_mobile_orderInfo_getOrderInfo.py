# coding:utf-8

from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data, _mobile_orderInfo_getClientOrderList # 85折订单列表
from api.mall_mobile_application._mobile_orderInfo_getOrderInfo import params, _mobile_orderInfo_getOrderInfo # 85折订单信息
from setting import P1, P2, P3, productCode

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
@allure.story("/mobile/orderInfo/getOrderInfo")
class TestClass:
    """
    通过订单号查询客户端订单信息
    /mobile/orderInfo/getOrderInfo
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.token_85 = os.environ["token_85"]

    @allure.severity(P1)
    @allure.title("通过订单号查询客户端订单信息-成功路径: 85折转分订单退货时查看订单信息检查")
    def test_mobile_orderInfo_getOrderInfo(self):
        
        getClientOrderList = None # 85折订单列表信息
        
        @allure.step("85折订单列表,获取订单号")
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
        
        step_mobile_orderInfo_getClientOrderList()
        step_mobile_orderInfo_getOrderInfo()
