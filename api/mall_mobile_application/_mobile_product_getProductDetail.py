# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


params = {
    "productCode": productCode, # 产品编码
}

def _mobile_product_getProductDetail(params=params, access_token=access_token):
    """
    商品详情
    /mobile/product/getProductDetail
    """

    url = f"{BASE_URL}/mobile/product/getProductDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r

response = {
	"code": 200,
	"message": "操作成功",
	"data": {
		"productId": "232", # 子产品id
		"serialNo": "M7035",
		"title": "玛丽艳活力精华露",
		"productType": 1, # 产品类型
		"productStatus": 7, # 商品状态 7-已上架,8-已下架
		"retailPrice": 480.00, # 零售价
		"exchangePrice": 480.00, # 换购价(废弃,取活动价)
		"activityPrice": None, # 活动价
		"underlinedPrice": 480.00, # 划线价
		"preDepositPrice": None,
		"depositDiscountPrice": None,
		"finalPaymentPrice": None,
		"pv": 410,
		"medais": [
            {"mediaType": 1,"url": "https://uc.oss.perfect99.com/mall-center-product/20210402160838QhPuD.png","sort": 1}, 
            {"mediaType": 1,"url": "https://uc.oss.perfect99.com/mall-center-product/20210402160842Xh1wA.png","sort": 2}, 
            {"mediaType": 1,"url": "https://uc.oss.perfect99.com/mall-center-product/20210402160842C7cGF.png","sort": 3}, 
            {"mediaType": 1,"url": "https://uc.oss.perfect99.com/mall-center-product/20210402160842xLtHo.png","sort": 4},
            {"mediaType": 1,"url": "https://uc.oss.perfect99.com/mall-center-product/20210402160842N1iVV.png","sort": 5}
        ],
		"serveContent": "1、收货时请当场验货，若商品有破损、渗漏、缺少、交付有误等问题，请立即与完美公司客服人员或分支机构联系。2、 消费者在购买产品30天内，将完好无损、具有销售价值的产品连同购货凭证一同退回，可按购货凭证价格等值换货或退款。3、若商品使用过程中怀疑出现质量问题，请立即与完美公司客服人员或分支机构联系，同时提供购货凭证及清晰的产品问题图片。4、金伟连牌净水机、宜悦牌空气净化机/器、德列宝系列（锅具、厨具）产品若消费者在使用过程中发生故障情况，请及时与完美公司客服人员或分支机构联系，具体售后服务规定详见《使用说明书》、《用户手册》。",
		"webContent": "<img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/DwAPpNyx84.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/kS4iGMicdn.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/5njnBXtaQG.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/bT2QFnJYBS.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/bkNT7JXwZB.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/z3yyWRiZeh.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/5HxySkaGxZ.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/fCGHN5TPfw.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/cnMADhE5QX.jpg\" alt=\"\" />",
		"appContent": "<img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/RPctiHTCsj.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/jbjMftEAiZ.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/NkmWSp7CMC.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/JR2bAarSj7.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/sS3k7kAc78.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/ZdakemxCaD.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/hbkzaARHkE.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/c2znYjYdYf.jpg\" alt=\"\" /><img src=\"https://uc.oss.perfect99.com/perfect-mall-1/prod/group1/hRWmnRbJFK.jpg\" alt=\"\" />",
		"customList": None,
		"bundleList": None,
		"releList": [],
		"recoList": [
            {
                "productId": "361",
                "title": "臻荟芦荟保湿舒缓面膜(30片装)",
                "serialNo": "AM00730",
                "imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402161513qN28S.png",
                "retailPrice": 398.00,
                "pv": 319,
                "isInvoice": 1,
                "isOneOrder": 0,
                "isProductReturn": 1,
                "isDeliver": 1,
                "orderWay": 2,
                "deliverWay": 2
            }, 
            {
                "productId": "1096",
                "title": "玛丽艳舒缓修护霜",
                "serialNo": "MA3036",
                "imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402161821Z9QIG.png",
                "retailPrice": 298.00,
                "pv": 255,
                "isInvoice": 1,
                "isOneOrder": 0,
                "isProductReturn": 1,
                "isDeliver": 1,
                "orderWay": 99,
                "deliverWay": 99
            }, 
            {
                "productId": "1091",
                "title": "玛丽艳滋润爽肤水",
                "serialNo": "MA5021",
                "imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402161232WwL7H.png",
                "retailPrice": 168.00,
                "pv": 144,
                "isInvoice": 1,
                "isOneOrder": 0,
                "isProductReturn": 1,
                "isDeliver": 1,
                "orderWay": 99,
                "deliverWay": 99
            }, 
            {
                "productId": "1063",
                "title": "玛丽艳维E润手霜",
                "serialNo": "MA8064",
                "imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402160646BXprt.png",
                "retailPrice": 63.00,
                "pv": 54,
                "isInvoice": 1,
                "isOneOrder": 0,
                "isProductReturn": 1,
                "isDeliver": 1,
                "orderWay": 99,
                "deliverWay": 99
            }, 
            {
                "productId": "1092",
                "title": "玛丽艳柔和洁肤乳",
                "serialNo": "MA5011",
                "imgUrl": "https://uc.oss.perfect99.com/mall-center-product/20210402161157LgTvc.png",
                "retailPrice": 0.01,
                "pv": 1,
                "isInvoice": 1,
                "isOneOrder": 0,
                "isProductReturn": 1,
                "isDeliver": 1,
                "orderWay": 99,
                "deliverWay": 2
            }
        ],
		"originalPrice": 480.00,
		"reduPrice": None,
		"stockMax": None,
		"stockRest": "-72084", # 已售数量
		"stockType": 2, # 库存类型, 1-限量 2-不限量
		"isShowStock": 0, # 是否显示库存, 0-否 1-是
		"isStopSale": 0, # 是否停止销售 0-否 1-是
		"isInvoice": 1, # 是否开发票 1-是，0-否
		"isOneOrder": 0, # 是否支持单独下单 1-是，0-否
		"isProductReturn": 1, # 是否支持可申请退货 1-是，0-否
		"isDeliver": 1, # 是否发货 1-是，0-否
		"isExchangeProduct": 0, # 是否换购商品 0-否 1-是
		"isPreProduct": 0, # 是否预售产品 1-是，0-否
		"isConsumeStock": 0, # 是否仅消耗服务中心库存 0-否 1-是
		"isInvalid": 0, # 是否已失效 0-否 1-是
		"orderWay": 99, # 下单方式 0-空, 1-自购,2-代购,99-全选
		"deliverWay": 99, # 交付方式 0-空, 1-公司交付,2-门店交付,99-全选
		"attrs": "{}",
		"attrList": [],
		"orderType": 1, # 订货类型 1-产品订货 2-资料订货 3-定制品订货
		"isActivateItem": 0, # 是否升级商品 1-是 0-否
		"purchaseLimitType": 0, # 限购类型 0-不限购 1-终身限购 2-每月限购
		"purchaseLimitNum": None,
		"isIdentityLimit": 0, # 是否身份限购 1-是 0-否
		"customerIdentityTypes": [],
		"customerCardTypes": []
	}
}