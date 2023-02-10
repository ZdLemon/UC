# coding:utf-8

from api.mall_mgmt_application._mgmt_store_getMasterMemberInfoByCardNo import params, _mgmt_store_getMasterMemberInfoByCardNo
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    根据会员卡号获取主顾客信息
    /mgmt/store/getMasterMemberInfoByCardNo
    """
    def setup_class(self):
        self.params = deepcopy(params)
        self.access_token = os.environ["access_token"]
    
    @allure.story("/mgmt/store/getMasterMemberInfoByCardNo")
    @allure.severity(P2)
    @allure.title("根据会员卡号获取主顾客信息-成功路径: 新建服务中心时录入负责人信息检查")
    def test_01_mgmt_store_getMasterMemberInfoByCardNo(self):
        
        params = deepcopy(self.params)
        params["cardNo"] = "3000003338"            
        with _mgmt_store_getMasterMemberInfoByCardNo(params, self.access_token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
            assert params["cardNo"] == "3000003338" == r.json()["data"]["cardNo"]