# coding:utf-8

from api.mall_mgmt_application._mgmt_inventory_dis_mortgage_common_fetchFreightTemplate import _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
@allure.story("/mgmt/inventory/dis/mortgage/common/fetchFreightTemplate")
class TestClass:
    """
    获取最新的运费计算模板
    /mgmt/inventory/dis/mortgage/common/fetchFreightTemplate
    """
    def setup_class(self):
        self.access_token = os.environ["access_token"]
               
    @allure.severity(P2)
    @allure.title("获取最新的运费计算模板-成功路径: 新建押货单时获取最新的运费检查")
    def test_mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(self):
                        
        with _mgmt_inventory_dis_mortgage_common_fetchFreightTemplate(self.access_token) as r:
            assert r.status_code == 200            
            assert r.json()["code"] == 200



