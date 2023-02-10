# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


data = {
    "storeCode": "", # 服务中心编号
    "storeName":None, # 服务中心名称
    "leaderNo":None, # 负责人卡号
    "leaderName":None, # 负责人姓名
    "companyCode":[], # 分公司code
    "settleAccount":None, # 结清账户 0未结清 1已结清
    "inventoryIsZero": "", # 库存是否为0: 0为0 1不为0
    "pageNum": 1,
    "changeStartDate": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01', # 经营模式切换开始日期 yyyy-MM-dd
    "changeEndDate": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]}' # 经营模式切换结束日期 yyyy-MM-dd 当月最后一天
}


def _mgmt_inventory_disInventoryTransfer_pageList(data=data, access_token=access_token):
    """
    押货转移管理列表
    /mgmt/inventory/disInventoryTransfer/pageList
    """

    url = f"{BASE_URL}/mgmt/inventory/disInventoryTransfer/pageList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
