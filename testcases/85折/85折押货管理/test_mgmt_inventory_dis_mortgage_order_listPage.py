# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_order_listPage import params, _mgmt_inventory_dis_mortgage_order_listPage
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/order/listPage")
class TestClass:
    """
    押货单列表查询
    /mgmt/inventory/dis/mortgage/order/listPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title(" 押货单列表查询-成功路径: 默认查询检查")
    def test_01_mgmt_inventory_dis_mortgage_order_listPage(self):
        
        params = deepcopy(self.params)                
        with _mgmt_inventory_dis_mortgage_order_listPage(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200

    @allure.severity(P2)
    @allure.title("押货单列表查询-成功路径: 查询是否交通管制检查")
    @pytest.mark.parametrize("isTrafficControl,ids", [(1, "是"), (2, "否")])
    def test_08_mgmt_inventory_dis_mortgage_order_listPage(self, isTrafficControl, ids):
                    
        params = deepcopy(self.params)
        params["isTrafficControl"] = isTrafficControl # 是否处于交通管制 0否 1是
        with _mgmt_inventory_dis_mortgage_order_listPage(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for i in set(d["isTrafficControl"] for d in r.json()["data"]["list"]):
                assert i == isTrafficControl
        
    @allure.severity(P2)
    @allure.title("后台查询押货退货单列表-成功路径: 查询物流评价检查")
    @pytest.mark.parametrize("logisticsEvaluation,ids", [(0, "未评价"), (1, "非常满意"), (2, "满意"), (3, "不满意")])
    def test_09_mgmt_inventory_dis_mortgage_order_listPage(self, logisticsEvaluation, ids):
                    
        params = deepcopy(self.params)
        params["logisticsEvaluation"] = logisticsEvaluation # 物流评价 0未评价 1非常满意 2满意 3不满意
        with _mgmt_inventory_dis_mortgage_order_listPage(params, self.access_token) as r:
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
    def test_10_mgmt_inventory_dis_mortgage_order_listPage(self, isLogisticsEvaluationReplied, ids):
                    
        params = deepcopy(self.params)
        params["isLogisticsEvaluationReplied"] = isLogisticsEvaluationReplied # 是否已回复物流评价 0未回复 1已回复
        with _mgmt_inventory_dis_mortgage_order_listPage(params, self.access_token) as r:
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
    def test_11_mgmt_inventory_dis_mortgage_order_listPage(self, isLogisticsFeedbackReplied, ids):
                    
        params = deepcopy(self.params)
        params["isLogisticsFeedbackReplied"] = isLogisticsFeedbackReplied # 是否已回复物流反馈 0未回复 1已回复
        with _mgmt_inventory_dis_mortgage_order_listPage(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            if r.json()["data"]["list"]:
                for i in set(d["isLogisticsFeedbackReplied"] for d in r.json()["data"]["list"]):
                    assert i == isLogisticsFeedbackReplied
            else:
                assert r.json()["data"]["list"] == []     


