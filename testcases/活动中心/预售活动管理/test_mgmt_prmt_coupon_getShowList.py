# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_selectPromotionListPage import params, _mgmt_prmt_selectPromotionListPage
from setting import P1, P2, P3, couponName, promotionName, promotionCode, productCode_ys

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/selectPromotionListPage")
class TestClass:
    """
    活动分页列表-预售活动
    /mgmt/prmt/selectPromotionListPage
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P3)
    @allure.title("预售活动列表-成功路径: 模糊搜索预售活动名称检查")
    @pytest.mark.parametrize("promotionName", [promotionName, promotionName[:-1]], ids=["预售活动完整名称", "预售活动名称的一部分"])
    def test_01_mgmt_prmt_selectPromotionListPage(self, promotionName):
                
        params = deepcopy(self.params)
        params["promotionName"] = promotionName            
        with _mgmt_prmt_selectPromotionListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert promotionName  in d["promotionName"]
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P3)
    @allure.title("预售活动列表-成功路径: 模糊搜索预售活动编号检查")
    @pytest.mark.parametrize("promotionCode", [promotionCode, promotionCode[:-1]], ids=["预售活动完整编号", "预售活动编号的一部分"])
    def test_02_mgmt_prmt_selectPromotionListPage(self, promotionCode):
                
        params = deepcopy(self.params)
        params["promotionCode"] = promotionCode            
        with _mgmt_prmt_selectPromotionListPage(params, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    assert promotionCode  in d["promotionCode"]
            else:
                assert r.json()["data"]["list"] == []
