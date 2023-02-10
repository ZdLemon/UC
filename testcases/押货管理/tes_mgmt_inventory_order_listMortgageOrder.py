# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_order_listMortgageOrder import params ,_mgmt_inventory_order_listMortgageOrder

from setting import P1, P2, P3, productCode_zh, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter
import calendar


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/order/listMortgageOrder")
class TestClass:
    """
    运营后台押货单列表查询
    /mgmt/inventory/order/listMortgageOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询本月检查")
    def test_01_mgmt_inventory_order_listMortgageOrder(self):
            
        params = deepcopy(self.params)
        params["beginTime"] = f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd 
        params["endTime"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_02_mgmt_inventory_order_listMortgageOrder(self):
            
        params = deepcopy(self.params) 
        storeCode = None 
        
        @allure.step("获取服务中心编号")
        def step_01_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal storeCode           
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                storeCode = r.json()["data"]["list"][0]["storeCode"]
        
        @allure.step("精确查询服务中心编号")
        def step_02_mgmt_inventory_order_listMortgageOrder():
            
            params["storeCode"] = storeCode
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
        
        @allure.step("模糊查询服务中心编号")
        def step_03_mgmt_inventory_order_listMortgageOrder():
            
            params["storeCode"] = storeCode[:-1]
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_order_listMortgageOrder()
        step_02_mgmt_inventory_order_listMortgageOrder()
        step_03_mgmt_inventory_order_listMortgageOrder()

    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 仅支持精确查询押货单号检查")
    def test_03_mgmt_inventory_order_listMortgageOrder(self):
            
        params = deepcopy(self.params) 
        orderSn = None 
        
        @allure.step("获取退货单号")
        def step_01_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal orderSn          
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderSn = r.json()["data"]["list"][0]["orderSn"]
        
        @allure.step("精确查询退货单号")
        def step_02_mgmt_inventory_order_listMortgageOrder():
            
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["orderSn"] for d in r.json()["data"]["list"]):
                    assert i == orderSn
        
        @allure.step("模糊查询退货单号")
        def step_03_mgmt_inventory_order_listMortgageOrder():
            
            params["storeCode"] = orderSn[:-1]
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_order_listMortgageOrder()
        step_02_mgmt_inventory_order_listMortgageOrder()
        step_03_mgmt_inventory_order_listMortgageOrder()

    @allure.severity(P3)
    @allure.title("后台查询押货退货单列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_04_mgmt_inventory_order_listMortgageOrder(self, companyCode):
                    
        params = deepcopy(self.params)
        params["companyCode"] = companyCode
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                assert i == companyCode
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询修改标记检查")
    @pytest.mark.parametrize("editFlag,ids", [(0, "普通押货退货"), (1, "套装组合退货")])
    def test_05_mgmt_inventory_order_listMortgageOrder(self, editFlag, ids):
                    
        params = deepcopy(self.params)
        params["editFlag"] = editFlag # 是否有修改过 0未修改 1已修改
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["editFlag"] for d in r.json()["data"]["list"]):
                assert i == editFlag
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询押货单来源检查")
    @pytest.mark.parametrize("orderSource,ids", [(1, "服务中心押货"), (2, "运营后台押货")])
    def test_06_mgmt_inventory_order_listMortgageOrder(self, orderSource, ids):
                    
        params = deepcopy(self.params)
        params["orderSource"] = orderSource # 押货单来源 1服务中心押货 2运营后台押货
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["orderSource"] for d in r.json()["data"]["list"]):
                assert i == orderSource
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询押货标识检查")
    @pytest.mark.parametrize("orderMark,ids", [(1, "普通押货单"), (2, "仅调账不发货"), (3, "套装组合押货"), (4, "套装拆分押货")])
    def test_07_mgmt_inventory_order_listMortgageOrder(self, orderMark, ids):
                    
        params = deepcopy(self.params)
        params["orderMark"] = orderMark # 标志 1普通押货单 2仅调账不发货 3套装组合押货 4套装拆分押货
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["orderMark"] for d in r.json()["data"]["list"]):
                assert i == orderMark
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询是否交通管制检查")
    @pytest.mark.parametrize("isTrafficControl,ids", [(1, "是"), (2, "否")])
    def test_08_mgmt_inventory_order_listMortgageOrder(self, isTrafficControl, ids):
                    
        params = deepcopy(self.params)
        params["isTrafficControl"] = isTrafficControl # 是否处于交通管制 0否 1是
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["isTrafficControl"] for d in r.json()["data"]["list"]):
                assert i == isTrafficControl
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询物流评价检查")
    @pytest.mark.parametrize("logisticsEvaluation,ids", [(0, "未评价"), (1, "非常满意"), (2, "满意"), (3, "不满意")])
    def test_09_mgmt_inventory_order_listMortgageOrder(self, logisticsEvaluation, ids):
                    
        params = deepcopy(self.params)
        params["logisticsEvaluation"] = logisticsEvaluation # 物流评价 0未评价 1非常满意 2满意 3不满意
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["logisticsEvaluation"] for d in r.json()["data"]["list"]):
                    assert i == logisticsEvaluation
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询是否已回复评价检查")
    @pytest.mark.parametrize("isLogisticsEvaluationReplied,ids", [(0, "未回复"), (1, "非已回复")])
    def test_10_mgmt_inventory_order_listMortgageOrder(self, isLogisticsEvaluationReplied, ids):
                    
        params = deepcopy(self.params)
        params["isLogisticsEvaluationReplied"] = isLogisticsEvaluationReplied # 是否已回复物流评价 0未回复 1已回复
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["isLogisticsEvaluationReplied"] for d in r.json()["data"]["list"]):
                    assert i == isLogisticsEvaluationReplied
            else:
                assert r.json()["data"]["list"] == []     
 
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询是否已回复反馈检查")
    @pytest.mark.parametrize("isLogisticsFeedbackReplied,ids", [(0, "未回复"), (1, "非已回复")])
    def test_11_mgmt_inventory_order_listMortgageOrder(self, isLogisticsFeedbackReplied, ids):
                    
        params = deepcopy(self.params)
        params["isLogisticsFeedbackReplied"] = isLogisticsFeedbackReplied # 是否已回复物流反馈 0未回复 1已回复
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["isLogisticsFeedbackReplied"] for d in r.json()["data"]["list"]):
                    assert i == isLogisticsFeedbackReplied
            else:
                assert r.json()["data"]["list"] == []     

     
@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/order/listMortgageOrder")
class TestClass02:
    """
    运营后台押货单列表查询-定制品押货查询
    /mgmt/inventory/order/listMortgageOrder
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询本月检查")
    def test_01_mgmt_inventory_order_listMortgageOrder(self):
            
        params = deepcopy(self.params)
        params["beginTime"] = f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # yyyy-MM-dd 
        params["endTime"] = time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 仅支持精确查询服务中心编号检查")
    def test_02_mgmt_inventory_order_listMortgageOrder(self):
            
        params = deepcopy(self.params) 
        params["customFlag:"] = 1
        storeCode = None 
        
        @allure.step("获取服务中心编号")
        def step_01_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal storeCode           
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                storeCode = r.json()["data"]["list"][0]["storeCode"]
        
        @allure.step("精确查询服务中心编号")
        def step_02_mgmt_inventory_order_listMortgageOrder():
            
            params["storeCode"] = storeCode
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["storeCode"] for d in r.json()["data"]["list"]):
                    assert i == storeCode
        
        @allure.step("模糊查询服务中心编号")
        def step_03_mgmt_inventory_order_listMortgageOrder():
            
            params["storeCode"] = storeCode[:-1]
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_order_listMortgageOrder()
        step_02_mgmt_inventory_order_listMortgageOrder()
        step_03_mgmt_inventory_order_listMortgageOrder()

    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 仅支持精确查询押货单号检查")
    def test_03_mgmt_inventory_order_listMortgageOrder(self):
            
        params = deepcopy(self.params)
        params["customFlag:"] = 1 
        orderSn = None 
        
        @allure.step("获取退货单号")
        def step_01_mgmt_inventory_order_listMortgageOrder():
            
            nonlocal orderSn          
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                orderSn = r.json()["data"]["list"][0]["orderSn"]
        
        @allure.step("精确查询退货单号")
        def step_02_mgmt_inventory_order_listMortgageOrder():
            
            params["orderSn"] = orderSn
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                for i in set(d["orderSn"] for d in r.json()["data"]["list"]):
                    assert i == orderSn
        
        @allure.step("模糊查询退货单号")
        def step_03_mgmt_inventory_order_listMortgageOrder():
            
            params["storeCode"] = orderSn[:-1]
            with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["data"]["list"] == []
        
        step_01_mgmt_inventory_order_listMortgageOrder()
        step_02_mgmt_inventory_order_listMortgageOrder()
        step_03_mgmt_inventory_order_listMortgageOrder()

    @allure.severity(P3)
    @allure.title("后台查询押货退货单列表-成功路径: 查询分公司编号检查")
    @pytest.mark.parametrize("companyCode", [f"0{i*1000}" if i <10 else f"{i*1000}" for i in range(2, 37) if i != 35])
    def test_04_mgmt_inventory_order_listMortgageOrder(self, companyCode):
                    
        params = deepcopy(self.params)
        params["companyCode"] = companyCode
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["companyCode"] for d in r.json()["data"]["list"]):
                assert i == companyCode
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询修改标记检查")
    @pytest.mark.parametrize("editFlag,ids", [(0, "普通押货退货"), (1, "套装组合退货")])
    def test_05_mgmt_inventory_order_listMortgageOrder(self, editFlag, ids):
                    
        params = deepcopy(self.params)
        params["editFlag"] = editFlag # 是否有修改过 0未修改 1已修改
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["editFlag"] for d in r.json()["data"]["list"]):
                assert i == editFlag
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询押货单来源检查")
    @pytest.mark.parametrize("orderSource,ids", [(1, "服务中心押货"), (2, "运营后台押货")])
    def test_06_mgmt_inventory_order_listMortgageOrder(self, orderSource, ids):
                    
        params = deepcopy(self.params)
        params["orderSource"] = orderSource # 押货单来源 1服务中心押货 2运营后台押货
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["orderSource"] for d in r.json()["data"]["list"]):
                assert i == orderSource
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询押货标识检查")
    @pytest.mark.parametrize("orderMark,ids", [(1, "普通押货单"), (2, "仅调账不发货"), (1, "套装组合押货"), (2, "套装拆分押货")])
    def test_07_mgmt_inventory_order_listMortgageOrder(self, orderMark, ids):
                    
        params = deepcopy(self.params)
        params["orderMark"] = orderMark # 标志 1普通押货单 2仅调账不发货 3套装组合押货 4套装拆分押货
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["orderMark"] for d in r.json()["data"]["list"]):
                assert i == orderMark
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询是否交通管制检查")
    @pytest.mark.parametrize("isTrafficControl,ids", [(1, "是"), (2, "否")])
    def test_08_mgmt_inventory_order_listMortgageOrder(self, isTrafficControl, ids):
                    
        params = deepcopy(self.params)
        params["isTrafficControl"] = isTrafficControl # 是否处于交通管制 0否 1是
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["isTrafficControl"] for d in r.json()["data"]["list"]):
                assert i == isTrafficControl
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询物流评价检查")
    @pytest.mark.parametrize("logisticsEvaluation,ids", [(0, "未评价"), (1, "非常满意"), (2, "满意"), (3, "不满意")])
    def test_09_mgmt_inventory_order_listMortgageOrder(self, logisticsEvaluation, ids):
                    
        params = deepcopy(self.params)
        params["logisticsEvaluation"] = logisticsEvaluation # 物流评价 0未评价 1非常满意 2满意 3不满意
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["logisticsEvaluation"] for d in r.json()["data"]["list"]):
                    assert i == logisticsEvaluation
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询是否已回复评价检查")
    @pytest.mark.parametrize("isLogisticsEvaluationReplied,ids", [(0, "未回复"), (1, "非已回复")])
    def test_10_mgmt_inventory_order_listMortgageOrder(self, isLogisticsEvaluationReplied, ids):
                    
        params = deepcopy(self.params)
        params["isLogisticsEvaluationReplied"] = isLogisticsEvaluationReplied # 是否已回复物流评价 0未回复 1已回复
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["isLogisticsEvaluationReplied"] for d in r.json()["data"]["list"]):
                    assert i == isLogisticsEvaluationReplied
            else:
                assert r.json()["data"]["list"] == []     
 
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询是否已回复反馈检查")
    @pytest.mark.parametrize("isLogisticsFeedbackReplied,ids", [(0, "未回复"), (1, "非已回复")])
    def test_11_mgmt_inventory_order_listMortgageOrder(self, isLogisticsFeedbackReplied, ids):
                    
        params = deepcopy(self.params)
        params["isLogisticsFeedbackReplied"] = isLogisticsFeedbackReplied # 是否已回复物流反馈 0未回复 1已回复
        params["customFlag:"] = 1
        with _mgmt_inventory_order_listMortgageOrder(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["isLogisticsFeedbackReplied"] for d in r.json()["data"]["list"]):
                    assert i == isLogisticsFeedbackReplied
            else:
                assert r.json()["data"]["list"] == []     

     





