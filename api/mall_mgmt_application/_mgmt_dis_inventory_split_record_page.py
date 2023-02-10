# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
	"product": "", # 商品编号
	"stopTime": [],
	"splitBegin": "",
	"splitEnd": "",
	"productCode": None,
	"pageNum": 1,
	"pageSize": 10
}


def _mgmt_dis_inventory_split_record_page(data=data, access_token=access_token):
    """
    查询套装拆分记录列表
    /mgmt/dis-inventory/split/record/page
    """

    url = f"{BASE_URL}/mgmt/dis-inventory/split/record/page"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
