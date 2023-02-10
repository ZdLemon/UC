# coding:utf-8

from api.mall_store_application._appStore_store_getSignBankAccountList import params, _appStore_store_getSignBankAccountList
from api.mall_store_application._appStore_invest import _appStore_invest
from setting import P1, P2, P3, username_85, store_85, name_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_store_application")
@allure.story("/appStore/invest")
class TestClass:
    """
     充值
    /appStore/invest
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.store_token = os.environ["store_token_85"]
               
    @allure.severity(P2)
    @allure.title("充值-成功路径: 工行充值检查")
    def test_appStore_invest(self, login_store_85):
        
        getSignBankAccountList = None # 签约银行列表
        payAmount = 10 # 充值金额
        
        @allure.step("获取签约银行列表")
        def step_appStore_store_getSignBankAccountList():
            
            nonlocal getSignBankAccountList
            params = deepcopy(self.params)                 
            with _appStore_store_getSignBankAccountList(params, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                getSignBankAccountList = r.json()["data"]
        
        @allure.step("充值")
        def step_appStore_invest():
        
            data = {
                "accountName": getSignBankAccountList[0]["accountName"], # 户名不能为空
                "bankAccount": getSignBankAccountList[0]["account"], # 代扣账户不能为空
                "bankName": getSignBankAccountList[0]["accountBank"], # 开户银行名称
                "businessType": 3, # 业务类型 1-> 库存转移支付 2->押货下单支付 3-> 充值
                "payAmount": payAmount, # 充值金额
                "payChannel": "WEB", # 充值渠道 WEB/APP
                "payType": 2, # 2->工行签约代扣 3->建行签约代扣
                "storeCode": login_store_85["data"]["storeCode"], # 店铺编号
                "userId": login_store_85["data"]["userId"] # 用户ID
            }                
            with _appStore_invest(data, self.store_token) as r:
                assert r.status_code == 200            
                assert r.json()["code"] == 200
                assert r.json()["message"] == "操作成功"
        
        step_appStore_store_getSignBankAccountList()
        step_appStore_invest()



