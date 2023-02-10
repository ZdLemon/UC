# coding:utf-8

from api.mall_mgmt_application._mgmt_store_getByParms import params, _mgmt_store_getByParms
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall_mgmt_application")
class TestClass:
    """
    根据常用条件查询服务中心
    /mgmt/store/getByParms
    """
    def setup_class(self):
        self.params = params
        self.access_token = os.environ["access_token"]
   
    @allure.story("/mgmt/store/getByParms")
    @allure.severity(P1)
    @allure.title("根据常用条件查询服务中心-成功路径: 点击【修改权限】按钮跳转检查")
    def test_mgmt_store_getByParms(self):
        
        params = deepcopy(self.params)
        params["storeCode"] = "903001"                
        with _mgmt_store_getByParms(params, self.access_token) as r:
            assert r.json() == {
                "code":200,
                "message":"操作成功",
                "data":[
                    {
                        "name":"北京中雅卓美咨询服务中心",
                        "leaderId":"900044751",
                        "leaderName":"黄熙晴",
                        "leaderCardNo":"00044751",
                        "code":"903001",
                        "companyName":"完美（中国）有限公司北京分公司",
                        "companyCode":"03000",
                        "shopType":9,
                        "frozenTime":None,
                        "frozenReason":"",
                        "cancelTime":1205205395000
                    }
                ]
            }
    
        
