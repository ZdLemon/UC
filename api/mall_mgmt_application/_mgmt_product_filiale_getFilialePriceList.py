# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, productCode

import requests


data = {
	"serialNo": productCode, # 商品编码
	"title": None, # 商品名称
	"priceCatalogId": None, # 所属类别id
	"minRetailPrice": None, # 零售价开始
	"maxRetailPrice": None, # 零售价结束
	"saleCompanyId": None, # 销售主体id
	"propertyRights": None, # 产权
	"productStatus": None, # 商品状态 6-待生效 7-已上架 8-已下架
	"timerange": None,
	"status": "5", # 0-待审核 1-已通过 2-未通过 3-已撤回 4-待添加 5-全部
	"pageNum": 1,
	"pageSize": 20
}

def _mgmt_product_filiale_getFilialePriceList(data=data, access_token=access_token):
    """
    分公司价格信息列表查询
    /mgmt/product/filiale/getFilialePriceList
    """

    url = f"{BASE_URL}/mgmt/product/filiale/getFilialePriceList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
