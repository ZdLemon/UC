# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
	"isDesc": 1, # 是否降序 1-是 0-否,默认为1
	"isProductNum": 1, # 只看有库存 1-是
	"isSelected": 0, # 只看已选 1-是(已选列表必传)
	"keyword": "", # 关键字
	"pageNum": 1,
	"pageSize": 10,
	"selectedList": [{ # 已选商品列表
		"serialNo": productCode, # 商品编码
		"selectNums": 2 # 数量
	}],
	"serialNo": None, # 商品编码
	"showId": "", # 分类id
	"sortBy": 0 # 0-库存，1-商品编码，2-单价与pv，3-数量(已选商品列表必传)，4-金额小计(已选商品列表必传),默认为0
}

def _mobile_product_discount_productList(data=data, access_token=access_token):
    """
    查询85折转分商品
    /mobile/product-discount/productList
    """

    url = f"{BASE_URL}/mobile/product-discount/productList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data
  
    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r




