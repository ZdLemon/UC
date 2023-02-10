# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_coupon_selectCouponNumber import params, _mgmt_prmt_coupon_selectCouponNumber
from api.mall_mgmt_application._mgmt_prmt_coupon_getShowList import _mgmt_prmt_coupon_getShowList
from setting import P1, P2, P3, couponName, couponNumber

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/prmt/coupon/selectCouponNumber")
class TestClass:
    """
    商品分类列表
    /mgmt/prmt/coupon/getShowList
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("商品分类列表-成功路径: 新建优惠券时商品分类列表检查")
    def test_mgmt_prmt_coupon_getShowList(self):
            
        @allure.step("查询优惠券编码是否已经存在")
        def step_mgmt_prmt_coupon_selectCouponNumber():
                
            params = deepcopy(self.params)             
            with _mgmt_prmt_coupon_selectCouponNumber(params, self.access_token) as r:
                assert r.status_code == 200
                if r.json()["code"] == 500:
                    assert r.json()["message"] == "优惠券编码不能重复"
                else:
                    assert r.json()["message"] == "操作成功"
        
        @allure.step("商品分类列表")
        def step_mgmt_prmt_coupon_getShowList():
                           
            with _mgmt_prmt_coupon_getShowList(self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
        
        step_mgmt_prmt_coupon_selectCouponNumber()
        step_mgmt_prmt_coupon_getShowList()

            
