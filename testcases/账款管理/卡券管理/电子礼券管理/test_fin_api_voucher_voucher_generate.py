# coding:utf-8

from api.basic_services._login import _login
from api.mall_center_finance._fin_api_voucher_voucher_generate import params, _fin_api_voucher_voucher_generate
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_center_finance")
@allure.story("/fin/api/voucher/voucher/generate")
class TestClass:
    """
    给会员生成电子礼券，方便测试
    /fin/api/voucher/voucher/generate
    """
    
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("给会员45722864生成10张电子礼券，方便测试")    
    def test_01_fin_api_voucher_voucher_generate(self, login_oauth_token):
        
        params = deepcopy(self.params)
        params["amount"] = 15
        params["memberId"] = login_oauth_token["data"]["userId"]
        params["beginTime"] = "2022-04-01 00:00:00"
        params["endTime"] = "2023-04-01 00:00:00"
        params["num"] = 1
        for i in range(10):
            with _fin_api_voucher_voucher_generate(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"
    
    @allure.severity(P1)
    @allure.title("给会员14498218生成10张电子礼券，方便测试")    
    def test_02_fin_api_voucher_voucher_generate(self, login_oauth_token_85):
        
        params = deepcopy(self.params)
        params["amount"] = 15
        params["memberId"] = login_oauth_token_85["data"]["userId"]
        params["beginTime"] = "2022-04-01 00:00:00"
        params["endTime"] = "2023-04-01 00:00:00"
        params["num"] = 1
        for i in range(10):
            with _fin_api_voucher_voucher_generate(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"

    @allure.severity(P1)
    @allure.title("给会员26712599生成10张电子礼券，方便测试")    
    def test_03_fin_api_voucher_voucher_generate(self, vip_login):
        
        params = deepcopy(self.params)
        params["amount"] = 15
        params["memberId"] =vip_login["data"]["userId"]
        params["beginTime"] = "2022-04-01 00:00:00"
        params["endTime"] = "2023-04-01 00:00:00"
        params["num"] = 1
        for i in range(10):
            with _fin_api_voucher_voucher_generate(params, self.access_token) as r:
                assert r.status_code == 200
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"
                
            