# coding:utf-8

from api.mall_mobile_application._mobile_orderInfo_getClientOrderList import data, _mobile_orderInfo_getClientOrderList # 客户端订单列表查询
from api.mall_mobile_application._mobile_web_order_as_applyAfterSale import params, _mobile_web_order_as_applyAfterSale
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall-mobile-application")
class TestClass:
    """
    申请售后是否支持退货、换货、维修、返修
    /mobile/web/order/as/applyAfterSale
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.params = deepcopy(params)
        self.data = deepcopy(data)

    @allure.story("/mobile/web/order/as/applyAfterSale")
    @allure.severity(P1)
    @allure.title("申请售后是否支持退货、换货、维修、返修-成功路径: 云商自购单申请售后是否支持退货、换货、维修、返修检查")
    def test_mobile_web_order_as_applyAfterSale(self):
        
        orderNo = None # 订单号
        
        @allure.step("客户端订单列表查询")
        def step_mobile_orderInfo_getClientOrderList():
            
            nonlocal orderNo
            
            data = deepcopy(self.data)
            data["queryType"] = None # 查询类型(默认为null) null->原有订单(包含85折订单)查询 1->85折转分订单 2->85折转分补报订单 3->85折转分订单+85折转分补报订单
            data["orderStatus"] = 2 # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成 默认空为全部        
            with _mobile_orderInfo_getClientOrderList(data, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200 
                orderNo = r.json()["data"]["list"][0]["orderNo"]
    
        @allure.step("客户端订单列表查询")
        def step_mobile_web_order_as_applyAfterSale():
            
            params = deepcopy(self.params)
            params["orderNo"] = orderNo
            with _mobile_web_order_as_applyAfterSale(params, self.token) as r:            
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["expressType"] == 1 # 配送方式 1->服务中心自提 2->公司配送
                assert r.json()["data"]["isExchange"] == 0 # 是否支持换货：1->是；0->否
                assert r.json()["data"]["isRepair"] == 0 # 是否支持维修：1->是；0->否
                assert r.json()["data"]["isReturn"] == 1 # 是否支持退货：1->是；0->否
                assert r.json()["data"]["isReturnRepair"] == 0 # 是否支持返修：1->是；0->否
                assert r.json()["data"]["isStoreClosed"] == 0 # 服务中心是否已结点：1->是；0->否
                assert r.json()["data"]["isStoreReturnOver"] == 0 # 服务中心是否超过退货限制：1->是；0->否
        
        step_mobile_orderInfo_getClientOrderList()
        step_mobile_web_order_as_applyAfterSale()