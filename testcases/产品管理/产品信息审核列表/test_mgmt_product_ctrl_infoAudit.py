# coding:utf-8

from api.mall_mgmt_application._mgmt_product_ctrl_listInfoAudit import data ,_mgmt_product_ctrl_listInfoAudit
from api.mall_mgmt_application._mgmt_product_ctrl_infoAudit import data as data02, _mgmt_product_ctrl_infoAudit
from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure
import pytest


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/ctrl/infoAudit")
@pytest.mark.skip()
class TestClass:
    """
    产品审核商品版本
    /mgmt/product/ctrl/infoAudit
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("产品审核商品版本-成功路径: 审核检查")
    @pytest.mark.parametrize("auditResult,ids", [(1, "审核通过"), (2, "审核不通过")])
    def test_mgmt_product_ctrl_infoAudit(self, auditResult, ids):
        
        versionId = None
        
        @allure.step("待产品审核商品版本列表：获取id")
        def step_mgmt_product_ctrl_listInfoAudit():
            
            nonlocal versionId
            data = deepcopy(self.data)
            data["auditStauts"] = 2
            with _mgmt_product_ctrl_listInfoAudit(data, self.access_token) as r:
                # 审核状态 2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-审核通过，7-已上架，8-已下架
                versionId = r.json()["data"]["list"][0]["id"]
        
        @allure.step("产品审核商品版本")
        def step_mgmt_product_ctrl_infoAudit():
            
            data = deepcopy(self.data02)
            data["versionId"] = versionId
            data["auditResult"] = auditResult
            with _mgmt_product_ctrl_infoAudit(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_product_ctrl_listInfoAudit()
        step_mgmt_product_ctrl_infoAudit()
