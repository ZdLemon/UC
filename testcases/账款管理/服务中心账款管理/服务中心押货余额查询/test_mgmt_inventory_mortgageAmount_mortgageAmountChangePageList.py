# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_listMortgageAmount import data , _mgmt_inventory_mortgageAmount_listMortgageAmount
from api.mall_mgmt_application._mgmt_inventory_mortgageAmount_mortgageAmountChangePageList import data as data02, _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList
from setting import P1, P2, P3, username, mobile, username_vip, store

from copy import deepcopy
import os
import allure
import pytest
import time
from operator import itemgetter


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/mortgageAmount/mortgageAmountChangePageList")
class TestClass:
    """
    服务中心账款管理 -- 押货余额详情(详情分页列表)
    /mgmt/inventory/mortgageAmount/mortgageAmountChangePageList
    """
    def setup_class(self):
        self.data02 = deepcopy(data02)
        self.access_token = os.environ["access_token"]

    @allure.severity(P2)
    @allure.title("押货余额详情: 默认查询交易月份=当月检查")
    def test_01_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(self):
        
        data = deepcopy(self.data02)                   
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                assert time.strftime("%Y-%m", time.localtime(int(d["updateTime"])/1000)) ==  data["startMonth"]
   
    @allure.severity(P2)
    @allure.title("押货余额详情: 查询报表字段检查")
    @pytest.mark.parametrize("reportType,ids", [(1, "汇/退押货款"), (2, "调整金额"), (3, "信誉额"), (14, "押货使用"), (15, "押货退货"), (17, "配送返还"), (18, "商城退货")])
    def test_02_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(self, reportType, ids):
        
        data = deepcopy(self.data02)
        data["reportType"] = reportType                     
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["tenType"] for d in r.json()["data"]["list"]):
                    if reportType == 1:
                        assert i in [1, 2, 12, 19]
                    elif reportType == 2:
                        assert i in [13, 16]
                    elif reportType in [3, 14, 15, 17, 18]:
                        assert i == reportType
            else:
                assert r.json()["data"]["list"] == []
    
    @allure.severity(P2)
    @allure.title("押货余额详情: 查询款项类型检查")
    @pytest.mark.parametrize("sevenBankType,ids", [(1, "汇押货款"), (2, "1:3押货款退款申请"), (3, "手工退押货款"), (4, "手工增押货款"), (5, "转销售"), (6, "钱包款与押货款互转"), (7, "其他"), (8, "押货保证金转移")])
    def test_03_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(self, sevenBankType, ids):
        
        data = deepcopy(self.data02)
        data["sevenBankType"] = sevenBankType                     
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for d in r.json()["data"]["list"]:
                    if sevenBankType == 1:                      # 汇押货款
                        assert d["tenType"] == 1                # 汇押货款
                        assert d["recordType"] in [1, 4, 5]     # 汇押货款，无法识别款确认押货款， 超额押货款确认押货款
                    elif sevenBankType == 2:                    # 1:3押货款退款申请
                        assert d["tenType"] == 2                # 退押货款
                        assert d["recordType"] in [2]           # 1:3押货款退款申请
                    elif sevenBankType == 3:                    # 手工退押货款
                        assert d["tenType"] == 2                # 退押货款
                        assert d["recordType"] in [7]           # 手工退押货款
                    elif sevenBankType == 4:                    # 手工增押货款
                        assert d["tenType"] == 1                # 汇押货款
                        assert d["recordType"] in [8]           # 手工增押货款
                    elif sevenBankType == 5:                    # 转销售
                        assert d["tenType"] == 2                # 退押货款
                        assert d["recordType"] in [9]           # 转销售
                    elif sevenBankType == 6:                    # 钱包款与押货款互转
                        if d["recordType"] == 11:               # 用钱包款还押货款
                            assert d["tenType"] == 1            # 汇押货款
                        else:                                   
                            assert d["tenType"] == 2            # 退押货款
                            d["recordType"] == 10               # 用押货款还钱包款
                    elif sevenBankType == 7:                    # 其他
                        assert d["tenType"] == 12               # 其他
                        assert d["recordType"] in [12]          # 其他
                    elif sevenBankType == 8:                    # 押货保证金转移
                        assert d["tenType"] == 19               # 押货保证金转移
                        assert d["recordType"] in [19]          # 押货保证金转移
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("押货余额详情: 查询交易类型检查")
    @pytest.mark.parametrize("tenType,ids", [
        (1, "汇押货款"), 
        (2, "退押货款"), 
        (3, "信誉额"), 
        (12, "其他"), 
        (13, "产品调价"), 
        (14, "押货使用"), 
        (15, "押货退货"), 
        (16, "押货调整"), 
        (17, "配送返还"), 
        (18, "商城退货"), 
        (19, "押货保证金转移")])
    def test_04_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(self, tenType, ids):
        
        data = deepcopy(self.data02)
        data["tenType"] = tenType                     
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, self.access_token) as r:
            if r.json()["data"]["list"]:
                for i in set(d["tenType"] for d in r.json()["data"]["list"]):
                    assert i == tenType
                for d in r.json()["data"]["list"]:
                    if tenType == 1:                            # 汇押货款
                        assert d["recordType"] in [1, 4, 5, 8, 11]  # 汇押货款，无法识别款确认押货款， 超额押货款确认押货款，手工增加押货款， 钱包款还押货款
                    elif tenType == 2:                          # 退押货款
                        assert d["recordType"] in [2, 7, 9, 10] # 1:3押货款退款申请，退押货款，转销售，押货款还钱包款
                    elif tenType == 12:                         # 其他
                        assert d["recordType"] in [12]          # 其他
                    elif tenType == 14:                         # 押货使用
                        assert d["recordType"] in [14]          # 押货支付
                    elif tenType == 15:                         # 押货退货
                        assert d["recordType"] in [15]          # 押货退货
                    elif tenType == 16:                         # 押货调整
                        assert d["recordType"] in [16]          # 押货调整
                    elif tenType == 17:                         # 配送返还
                        assert d["recordType"] in [17]          # 商城订单转押货额
                    elif tenType == 18:                         # 商城退货
                        assert d["recordType"] in [18]          # 商城退货减押货额
                    elif tenType == 19:                         # 押货保证金转移
                        assert d["recordType"] in [8]           # 押货保证金转移
                    else:                                       
                        assert d["recordType"] is None          
            else:
                assert r.json()["data"]["list"] == []

    @allure.severity(P2)
    @allure.title("押货余额详情: 查询单号或流水号检查")
    def test_05_mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(self):
        
        data = deepcopy(self.data02)                   
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, self.access_token) as r:
            businessId = r.json()["data"]["list"][0]["businessId"]
        
        data["bizNo"] = businessId
        with _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            for d in r.json()["data"]["list"]:
                assert d["businessId"] == businessId


 