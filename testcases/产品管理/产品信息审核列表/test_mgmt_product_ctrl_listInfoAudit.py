# coding:utf-8

from api.mall_mgmt_application._mgmt_product_ctrl_listInfoAudit import data ,_mgmt_product_ctrl_listInfoAudit

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/ctrl/listInfoAudit")
class TestClass:
    """
    待产品审核待产品审核商品版本列表
    /mgmt/product/ctrl/listInfoAudit
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("待产品审核商品版本列表-成功路径: 支持大小写查询产品编号检查")
    @pytest.mark.parametrize("serialNo,ids", [(productCode_zh, "大写字母产品编号"), (productCode_zh.lower(), "小写字母产品编号")])
    def test_01_mgmt_product_ctrl_listInfoAudit(self, serialNo, ids):

        
        data = deepcopy(self.data)
        data["serialNo"] = serialNo
        with _mgmt_product_ctrl_listInfoAudit(data, self.access_token) as r:
            assert r.json()["data"]["list"][0]["serialNo"] == productCode_zh

    @allure.severity(P2)
    @allure.title("待产品审核商品版本列表-成功路径: 支持模糊查询产品名称检查")
    @pytest.mark.parametrize("title", [productCode_zh_title, productCode_zh_title[:-2]], ids=["完整的产品名称", "产品名称的一部分"])
    def test_02_mgmt_product_ctrl_listInfoAudit(self, title):
        
        data = deepcopy(self.data)   
        data["title"] = title                   
        with _mgmt_product_ctrl_listInfoAudit(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert title in d["title"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("待产品审核商品版本列表-成功路径: 查询时间检查")
    def test_03_mgmt_product_ctrl_listInfoAudit(self):
        
        data = deepcopy(self.data)  
        data["startTime"] = int(round(time.mktime(time.strptime(f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01 00:00:00", "%Y-%m-%d %H:%M:%S")) * 1000))
        data["endTime"] = int(round(time.mktime(time.strptime(f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))} 23:59:59", "%Y-%m-%d %H:%M:%S")) * 1000))   
        with _mgmt_product_ctrl_listInfoAudit(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert int(data["startTime"]) <= int(d["createTime"]) <= int(data["endTime"])
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("待产品审核商品版本列表-成功路径: 查询审核状态检查")
    @pytest.mark.parametrize("auditStauts,ids", [(2, "待审核"), (3, "已通过"), (4, "不通过")])
    def test_04_mgmt_product_ctrl_listInfoAudit(self, auditStauts, ids):
       
        data = deepcopy(self.data)
        data["auditStauts"] = auditStauts
        with _mgmt_product_ctrl_listInfoAudit(data, self.access_token) as r:
            # 审核状态 2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-审核通过，7-已上架，8-已下架
            for i in set(d["statusNote"] for d in r.json()["data"]["list"]):
                assert i == ids
