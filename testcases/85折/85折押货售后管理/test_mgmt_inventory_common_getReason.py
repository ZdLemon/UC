# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_common_getReason import params, _mgmt_inventory_common_getReason
from setting import P1, P2, P3, store_85

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/common/getReason")
class TestClass:
    """
    获取各种退换货原因
    /mgmt/inventory/common/getReason
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("获取各种退换货原因-成功路径: 获取各种退换货原因检查")
    def test_mgmt_inventory_common_getReason(self):
        
        params = deepcopy(self.params)                
        with _mgmt_inventory_common_getReason(params, self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200
            assert r.json() == {
                "code": 200,
                "message": "操作成功",
                "data": [{
                    "id": "200000000003",
                    "returnType": 3,
                    "returnReason": "结点退货",
                    "parentReasonId": "0",
                    "reasonList": [{
                        "id": "1251048643891483739",
                        "returnType": 3,
                        "returnReason": "结点库存退货",
                        "parentReasonId": "200000000003"
                    }, {
                        "id": "1251048643891483851",
                        "returnType": 3,
                        "returnReason": "结点库存六折平账",
                        "parentReasonId": "200000000003"
                    }, {
                        "id": "1251048643891483852",
                        "returnType": 3,
                        "returnReason": "转油葱微店六折平账",
                        "parentReasonId": "200000000003"
                    }, {
                        "id": "1251048643891483853",
                        "returnType": 3,
                        "returnReason": "转油葱微店库存退货",
                        "parentReasonId": "200000000003"
                    }]
                }, {
                    "id": "200000000005",
                    "returnType": 3,
                    "returnReason": "其他原因退货",
                    "parentReasonId": "0",
                    "reasonList": [{
                        "id": "1251048643891483740",
                        "returnType": 3,
                        "returnReason": "公司调整押货额退货",
                        "parentReasonId": "200000000005"
                    }, {
                        "id": "1251048643891483800",
                        "returnType": 3,
                        "returnReason": "特批退货",
                        "parentReasonId": "200000000005"
                    }, {
                        "id": "1251048643891483801",
                        "returnType": 3,
                        "returnReason": "优惠活动账面调账退货",
                        "parentReasonId": "200000000005"
                    }]
                }, {
                    "id": "1251048643891483848",
                    "returnType": 3,
                    "returnReason": "误押或滞压货退货",
                    "parentReasonId": "0",
                    "reasonList": [{
                        "id": "1251048643891483849",
                        "returnType": 3,
                        "returnReason": "90天内误押或滞压退货",
                        "parentReasonId": "1251048643891483848"
                    }]
                }]
            }
