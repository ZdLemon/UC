# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_deleteCacheMember import _mgmt_prmt_deleteCacheMember
from api.mall_mgmt_application._mgmt_prmt_selectPromotionCode import _mgmt_prmt_selectPromotionCode
from setting import P1, P2, P3, couponName, promotionName, promotionCode

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/selectPromotionCode")
class TestClass:
    """
    查询活动编码是否已经存在
    /mgmt/prmt/selectPromotionCode
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]

    @allure.severity(P3)
    @allure.title("查询活动编码是否已经存在-成功路径: 查询活动编码是否已经存在检查")
    def test_mgmt_prmt_selectPromotionCode(self):
        
        @allure.step("删除缓存的活动用户")
        def step_mgmt_prmt_deleteCacheMember():
            
            data = {
                "id": None
            }                  
            with _mgmt_prmt_deleteCacheMember(data, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        @allure.step("查询活动编码是否已经存在")
        def step_mgmt_prmt_selectPromotionCode():
            
            params = {
                "promotionCode": promotionCode, # 活动编码
                "promotionId": None,
            }                  
            with _mgmt_prmt_selectPromotionCode(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 500
                assert r.json()["message"] == "活动编码不能重复"
                
        step_mgmt_prmt_deleteCacheMember()
        step_mgmt_prmt_selectPromotionCode()
        
        
        
        



            
