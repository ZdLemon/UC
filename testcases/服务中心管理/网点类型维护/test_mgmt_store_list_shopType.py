# coding:utf-8

from api.mall_mgmt_application._mgmt_store_list_shopType import params, _mgmt_store_list_shopType
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/store/list/shopType")
class TestClass:
    """
    网点类型列表
    /mgmt/store/list/shopType
    """
    def setup_class(self):
        self.params = params
        self.access_token = os.environ["access_token"]
   
    @allure.severity(P2)
    @allure.title("网点类型列表-成功路径: 网点类型列表检查")
    def test_mgmt_store_list_shopType(self):
        
        params = deepcopy(self.params)              
        with _mgmt_store_list_shopType(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json() == {
                "code": 200,
                "message": "操作成功",
                "data": {
                    "pageNum": 1,
                    "pageSize": 20,
                    "totalPage": 1,
                    "total": 16,
                    "list": [
                        {
                        "id": 1,
                        "type": 1,
                        "name": "正式网点",
                        "remark": "正式网点"
                        }, 
                        {
                        "id": 2,
                        "type": 2,
                        "name": "正式网点/申请微店中",
                        "remark": "正式网点/申请微店"
                        }, 
                        {
                        "id": 3,
                        "type": 3,
                        "name": "正式网点（美容中心转）",
                        "remark": "正式网点（美容中心转）"
                        }, 
                        {
                        "id": 4,
                        "type": 4,
                        "name": "油葱微店（已取消未结清账务）",
                        "remark": "油葱微店（已取消未结清账务）"
                        }, 
                        {
                        "id": 5,
                        "type": 5,
                        "name": "油葱微店测试",
                        "remark": "油葱微店测试"
                        }, 
                        {
                        "id": 6,
                        "type": 6,
                        "name": "油葱微店（结点/取消）",
                        "remark": "油葱微店（结点/取消）"
                        },
                        {
                        "id": 7,
                        "type": 7,
                        "name": "油葱微店（冻结)",
                        "remark": "油葱微店（冻结)"
                        },
                        {
                        "id": 8,
                        "type": 8,
                        "name": "油葱微店（办理中）",
                        "remark": "油葱微店（办理中）"
                        },
                        {
                        "id": 9,
                        "type": 9,
                        "name": "油葱微店",
                        "remark": "油葱微店"
                        },
                        {
                        "id": 10,
                        "type": 10,
                        "name": "已取消（未结清账务）",
                        "remark": "已取消（未结清账务）"
                        },
                        {
                        "id": 11,
                        "type": 11,
                        "name": "新批未运作",
                        "remark": "新批未动作"
                        }, 
                        {
                        "id": 12,
                        "type": 12,
                        "name": "结点/取消",
                        "remark": "结点/取消"
                        }, 
                        {
                        "id": 13,
                        "type": 13,
                        "name": "冻结资格/申请微店中",
                        "remark": "冻结资格/申请微店中"
                        },
                        {
                        "id": 14,
                        "type": 14,
                        "name": "冻结资格（美容中心转）",
                        "remark": "冻结资格（美容中心转）"
                        },
                        {
                        "id": 15,
                        "type": 15,
                        "name": "冻结资格",
                        "remark": "冻结资格"
                        }, 
                        {
                        "id": 16,
                        "type": 16,
                        "name": "办理结点中",
                        "remark": "办理结点中"
                        }
                    ]
                }
            }
        
