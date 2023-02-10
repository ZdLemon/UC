# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
	"addressId": None,
	"customerCard": "3000002095", # 给某个顾客下单的会员卡号(不是指下单人)
	"customerId": "1270780218333982428", # 给某个顾客下单的会员ID
	"expressType": 1, # 配送方式 1->服务中心自提 2->公司配送
	"orderAmount": 480, # 商品金额,提交订单时必传
	"productList": [{
		"releList": None,
		"imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png",
		"title": "玛丽艳活力精华露",
		"serialNo": "M7035",
		"activityPrice": 480,
		"quantity": 1,
		"pv": 410,
		"productType": 1,
		"isActivateItem": 0,
		"retailPrice": 480,
		"isActivity": 0,
		"number": 1
	}],
	"orderInvoice": None, # 发票信息
	"couponList": [],
	"giftList": [],
	"freightList": [],
	"secondCouponList": [],
	"storeCode": "942437", # 服务中心编码
	"ownerId": "", # 送货人ID
	"pv": 410,
	"remarks": "",
	"returnRate": 0.12, # 返还比例,提交订单时必传
	"sharerId": None, # 分享人id
	"sourceType": 1, # 0(立即购买),1(快速购货),2(购物车提交),3(结算前销售调整),4(定制商品购买),5(辅销品购买),6(旧版商品购买),7(调差购买),8(85折转分订单),9(85折转分补报订单),10(单位团购报单)
	"isUpgrade": 0 # 是否升级单 0->否 1->是
}

def _mobile_trade_orderCommit(data=data, access_token=access_token):
    """
    提交订单
    /mobile/trade/orderCommit
    """

    url = f"{BASE_URL}/mobile/trade/orderCommit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r

response = {
	"code": 200,
	"message": "操作成功",
	"data": {
		"orderNo": "SG942437220325000011",
		"depositNo": None,
		"orderStatus": 1, # 订单状态 0->待审核 1->待支付 2->待发货 3->待收货 4->已取消 5->已退货 98->审核取消 99->已完成
		"orderDeposit": None,
		"totalAmount": 480.00, # 实付金额=订单金额-返还金额-优惠券-电子礼券-运费补贴券+运费
		"orderAmount": 480.00, # 应付金额=单价*数量
		"discountAmount": 0.00, # 优惠金额
		"balanceAmount": None,
		"actuallyBalanceAmount": None,
		"sysCancelTime": None, # 自动取消订单时间
		"commitTime": 1648207686526, # 开单时间
		"customerName": "李思", # 顾客姓名
		"customerCard": "3000002095", # 顾客卡号
		"isUpgrade": 0, # 是否升级单 0->否 1->是
		"isOldOrder": False, # 是否旧订单
		"unsatisfiedList": None, # 库存不足产品列表
		"nonSupport85ProductList": None # 不支持85折订单商品列表
	}
}


