# coding:utf-8

from api.mall_mobile_application._mobile_msg_manage_letter_dashbord import params, _mobile_msg_manage_letter_dashbord
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    用户站内信列表,按消息类型分类
    /mobile/msg/manage/letter/dashbord/{usrId}/{systemId}
    """
    def setup_class(self):
        self.token = os.environ["token"]
        self.params = deepcopy(params)

    @allure.story("/mobile/msg/manage/letter/dashbord")
    @allure.severity(P1)
    @allure.title("用户站内信列表,按消息类型分类-成功路径: 站内信检查")
    def test_mobile_msg_manage_letter_dashbord(self):

        params = deepcopy(self.params)
        with _mobile_msg_manage_letter_dashbord(params, self.token) as r:            
            assert r.status_code == 200
            assert r.json()["code"] == 200
                


