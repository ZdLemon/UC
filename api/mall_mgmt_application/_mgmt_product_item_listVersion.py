# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"versionStatus": "", # 状态：1-草稿，2-待产品审核，3-产品审核不通过，4-待财务审核，5-财务审核不通过，6-待生效，7-已上架，8-已下架
	"pageNum": 1,
	"pageSize": 10,
	"serialNo": "", # 商品编码
	"title": None, # 商品名称
	"catalogId": None, # 类型id
	"saleCompanyId": None, # 销售主体id
	"orderType": None, # 订单类型，1-产品订货，2-资料订货，3-订制品订货
	"directSale": None, # 是否直销，1-是，0-否
	"orderWay": None, # 下单方式 1-自购,2-代购
	"deliverWay": None, # 交付方式 1-公司交付,2-门店交付
	"startTime": "", # 开始时间时间戳
	"endTime": "" # 结束时间时间戳
}

def _mgmt_product_item_listVersion(data=data, access_token=access_token):
    """
    商品版本列表
    /mgmt/product/item/listVersion
    """

    url = f"{BASE_URL}/mgmt/product/item/listVersion"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
