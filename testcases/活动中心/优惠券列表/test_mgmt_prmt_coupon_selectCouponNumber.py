# coding:utf-8

from api.mall_mgmt_application._mgmt_prmt_coupon_selectCouponNumber import params ,_mgmt_prmt_coupon_selectCouponNumber

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
    查询优惠券编码是否已经存在
    /mgmt/prmt/coupon/selectCouponNumber
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("查询优惠券编码是否已经存在-成功路径: 新建优惠券时查询优惠券编码是否已经存在检查")
    def test_mgmt_prmt_coupon_selectCouponNumber(self):
            
        params = deepcopy(self.params)             
        with _mgmt_prmt_coupon_selectCouponNumber(params, self.access_token) as r:
            assert r.status_code == 200
            if r.json()["code"] == 500:
                assert r.json()["message"] == "优惠券编码不能重复"
            else:
                assert r.json()["message"] == "操作成功"
            
