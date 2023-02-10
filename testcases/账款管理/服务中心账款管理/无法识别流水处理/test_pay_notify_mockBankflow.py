# coding:utf-8

from api.basic_services._login import _login
from api.mall_center_pay._pay_notify_mockBankflow import data, _pay_notify_mockBankflow
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure
import time


@allure.feature("mall_center_pay")
@allure.story("/pay/notify/mockBankflow")
class TestClass:
    """
    模拟线下汇款
    /pay/notify/mockBankflow
    """
    
    def setup_class(self):
        self.data = deepcopy(data)
        self.access_token = os.environ["access_token"]
    
    @allure.severity(P1)
    @allure.title("给会员14498218生成自动识别流水")    
    def test_01_pay_notify_mockBankflow(self):
        
        data = deepcopy(self.data)
        with _pay_notify_mockBankflow(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.text == "SUCCESS"

    @allure.severity(P2)
    @allure.title("生成无法识别流水，方便测试")    
    def test_02_pay_notify_mockBankflow(self):
        
        data = deepcopy(self.data)
        data[0]["accountName"] = "我是无法识别的银行账户"
        data[0]["accountNo"] = "622123456789951753"
        data[0]["bankName"] = "中国工商银行深圳华南城支行"
        with _pay_notify_mockBankflow(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.text == "SUCCESS"

    @allure.severity(P2)
    @allure.title("批量生成自动识别流水，方便测试")    
    def test_03_pay_notify_mockBankflow(self):
        
        data = [
            {
                "accountName": "玩物志天",
                "accountNo": '622123456789369852',
                "bankName": "玩物志天",
                "busiTime": f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))}T00:00:00.261+0800",
                "companyNo": '02000',
                "receiptAccount": '3602028919200120721',
                "receiptBankName": "中国工商银行",
                "remark": None,
                "tradeAmount": '21',
                "tradeOrderNo": f"HK{str(time.time() * 1000)[:13]}",
            },
            {
                "accountName": "玩物志天",
                "accountNo": '622123456789369852',
                "bankName": "玩物志天",
                "busiTime": f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))}T00:00:00.261+0800",
                "companyNo": '02000',
                "receiptAccount": '3602028919200120721',
                "receiptBankName": "中国工商银行",
                "remark": None,
                "tradeAmount": '22',
                "tradeOrderNo": f"HK{str(time.time() * 1000)[:13]}",
            },
            {
                "accountName": "玩物志天",
                "accountNo": '622123456789369852',
                "bankName": "玩物志天",
                "busiTime": f"{time.strftime('%Y-%m-%d',time.localtime(time.time()))}T00:00:00.261+0800",
                "companyNo": '02000',
                "receiptAccount": '3602028919200120721',
                "receiptBankName": "中国工商银行",
                "remark": None,
                "tradeAmount": '23',
                "tradeOrderNo": f"HK{str(time.time() * 1000)[:13]}",
            },
            ]
        with _pay_notify_mockBankflow(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.text == "SUCCESS"

