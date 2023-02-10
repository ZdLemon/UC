# coding:utf-8

from api.mall_mgmt_application._mgmt_product_item_listVersion import data ,_mgmt_product_item_listVersion
from api.mall_mgmt_application._mgmt_product_item_getVersion import params ,_mgmt_product_item_getVersion

from setting import P1, P2, P3, productCode_zh, productCode_zh_title, productCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/product/item/listVersion")
class TestClass:
    """
    商品版本列表
    /mgmt/product/item/listVersion
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 支持模糊查询产品编号检查")
    def test_01_mgmt_product_item_listVersion(self):

        
        data = deepcopy(self.data)
        params = deepcopy(self.params)
        data["serialNo"] = productCode
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if d["serialNo"].startswith(productCode):
                        assert productCode in d["serialNo"]
                    else:                        
                        params["verId"] = str(d["id"])         
                        with _mgmt_product_item_getVersion(params, self.access_token) as r:
                            assert productCode in  set(d["serialNo"] for d in r.json()["data"]["bundleProductInfos"])
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 支持模糊查询产品名称检查")
    @pytest.mark.parametrize("title", [productCode_zh_title, productCode_zh_title[:-2]], ids=["完整的产品名称", "产品名称的一部分"])
    def test_02_mgmt_product_item_listVersion(self, title):
        
        data = deepcopy(self.data)   
        data["title"] = title                   
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert title in d["title"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 下拉查询产品类型检查")
    @pytest.mark.parametrize("catalogId,ids", [
        (10, "小型厨具"), 
        (5, "健康食品"), 
        (6, "服务中心物料"), 
        (7, "服务中心赠品"), 
        (8, "辅销资料"), 
        (9, "积分换购"), 
        (2, "保洁用品及个人护理品"),
        (3, "化妆品(玛丽艳美容护肤品)"),
        (4, "保健器材"), 
        (12, "赠送资料"), 
        (14, "辅销品")
    ])
    def test_03_mgmt_product_item_listVersion(self, catalogId, ids):
        
        data = deepcopy(self.data)   
        data["catalogId"] = str(catalogId)          
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["catalogId"] for d in r.json()["data"]["list"]):
                    assert i == str(catalogId)
            else:
                assert r.json()["data"]["list"] == []      

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 下拉查询销售主体检查")
    @pytest.mark.parametrize("saleCompanyId,ids", [(2, "完美中国"), (3, "上海商业"), (5, "上海健康")])
    def test_04_mgmt_product_item_listVersion(self, saleCompanyId, ids):
        
        data = deepcopy(self.data)   
        data["saleCompanyId"]= str(saleCompanyId)          
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["saleCompanyId"] for d in r.json()["data"]["list"]):
                    assert i == str(saleCompanyId)
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 下拉查询订货类型检查")
    @pytest.mark.parametrize("orderType,ids", [(1, "产品订货"), (2, "资料订货"), (3, "定制品订货")])
    def test_05_mgmt_product_item_listVersion(self, orderType, ids):
        
        data = deepcopy(self.data)   
        data["orderType"] = orderType                 
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["orderType"] for d in r.json()["data"]["list"]):
                    assert i == orderType
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 下拉查询是否直销产品检查")
    @pytest.mark.parametrize("directSale,ids", [(0, "非直销产品"), (1, "直销产品")])
    def test_06_mgmt_product_item_listVersion(self, directSale, ids):
        
        data = deepcopy(self.data)   
        data["directSale"] = directSale                    
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["directSale"] for d in r.json()["data"]["list"]):
                    assert i == directSale
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 下拉查询下单方式检查")
    @pytest.mark.parametrize("orderWay,ids", [(1, "自购"), (2, "代购")])
    def test_07_mgmt_product_item_listVersion(self, orderWay, ids):
        
        data = deepcopy(self.data)   
        data["orderWay"] = orderWay                    
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["orderWay"] for d in r.json()["data"]["list"]):
                    assert i == orderWay
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("商品版本列表-成功路径: 下拉查询交付方式检查")
    @pytest.mark.parametrize("deliverWay,ids", [(1, "公司交付"), (2, "门店交付")])
    def test_08_mgmt_product_item_listVersion(self, deliverWay, ids):
        
        data = deepcopy(self.data)   
        data["deliverWay"] = deliverWay                    
        with _mgmt_product_item_listVersion(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["deliverWay"] for d in r.json()["data"]["list"]):
                    assert i == deliverWay
            else:
                assert r.json()["data"]["list"] == []







