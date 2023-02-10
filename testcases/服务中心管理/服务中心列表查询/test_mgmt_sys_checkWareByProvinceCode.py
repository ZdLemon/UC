# coding:utf-8

from api.mall_center_sys._mgmt_sys_checkWareByProvinceCode import params, _mgmt_sys_checkWareByProvinceCode
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_center_sys")
class TestClass:
    """
    查询所在地是否存在可用仓库
    /mgmt/sys/checkWareByProvinceCode
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/sys/checkWareByProvinceCode")
    @allure.severity(P2)
    @allure.title("查询所在地是否存在可用仓库-成功路径: 查询有仓库的地方,返回True")
    def test_mgmt_sys_checkWareByProvinceCode(self):
        
        params = deepcopy(self.params)                
        with _mgmt_sys_checkWareByProvinceCode(params, self.access_token) as r:
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert r.json()["message"] == "操作成功"
            assert r.json()["data"] == True
 