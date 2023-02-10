# coding:utf-8

from api.mall_mobile_application._mobile_order_carts_toSettlement import data, _mobile_order_carts_toSettlement
from api.mall_mobile_application._mobile_product_search import data as data01, _mobile_product_search
from setting import P1, P2, P3

from copy import deepcopy
import os
import allure


@allure.feature("mall-mobile-application")
class TestClass:
    """
    选择商品去结算
    /mobile/order/carts/toSettlement
    """
    def setup_class(self):
        self.data = deepcopy(data)
        self.data01 = deepcopy(data01)
        self.token = os.environ["token"]

    @allure.story("/mobile/order/carts/toSettlement")
    @allure.severity(P1)
    @allure.title("选择商品去结算-成功路径: 云商自购下单,不使用任何优惠时选择商品结算检查")
    def test_mobile_order_carts_toSettlement(self, login_oauth_token):
        
        user = login_oauth_token["data"] # 开单人信息
        product = None # 产品信息
        
        @allure.step("搜索商品,获取产品信息")
        def step_mobile_product_search():

            nonlocal product
            data = deepcopy(self.data01)
            with _mobile_product_search(data, self.token) as r:            
                assert r.status_code == 200
                product = r.json()["data"]["list"][0] # 产品信息
        
        @allure.step("选择商品去结算")
        def step_mobile_order_carts_toSettlement():

            data = deepcopy(self.data)
            data = {
                "addressId": None,  # 收货地址id
                "customerCard": user["cardNo"],  # 开单人
                "customerId": user["userId"],  # 开单人id
                "expressType": 1,  # 配送方式 1->服务中心自提 2->公司配送
                "orderAmount": product["retailPrice"],  # 商品金额,提交订单时必传
                "productList": [  # 购买产品信息
                        {
                            "releList": None,
                            "imgUrl": product["imgUrl"],
                            "title": product["title"],
                            "serialNo": product["serialNo"],  # 产品编码
                            "retailPrice": product["retailPrice"],  # 产品价格"
                            "quantity": 1,  # 数量
                            "pv": product["pv"],
                            "productType": product["productType"],
                            "number": 1  # 换购商品数量
                        }
                ],
                "orderInvoice": None,  # 发票信息
                "couponList": [],  # 使用的优惠卷
                "giftList": [],  # 使用的电子礼券
                "freightList": [],  # 使用的运费补贴礼券
                "storeCode": user["storeCode"],  # 服务中心编码
                "ownerId": "",  # 送货人ID
                "pv": product["pv"],
                "remarks": "",  # 备注
                "returnRate": 0.12,  # 返还比例,提交订单时必传
                "sharerId": None,  # 分享人id
                "sourceType": 1  # 1(立即购买/快速购货)，2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买)
            }         
            with _mobile_order_carts_toSettlement(data, self.token) as r:            
                assert r.status_code == 200 
        
        step_mobile_product_search()
        step_mobile_order_carts_toSettlement()
        


