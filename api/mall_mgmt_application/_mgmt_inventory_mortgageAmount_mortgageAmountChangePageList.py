# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store

import requests
import time

"""
19种底层款项类型 全部则为空 1汇押货款、2 1:3押货退款申请、3超额押货款退款、4超额押货款确认押货款、5无法识别款确认押货款、
6无法识别款退款、7手工退押货款、8手工增加押货款、9转销售、10押货款还钱包欠款、
11钱包款还押货欠款、12其它 13产品调价 14押货支付 15押货退货 
16押货调整 17商城订单转押货额 18商城退货减押货额 19押货保证金转移
"""

data = {
    "storeCode": store, # 服务中心编号
    "reportType":None, # 7种报表映射类型 0 -> 全部 1-> 汇/退押货款 2->调整金额 3-> 信誉额 14-> 押货使用 15-> 押货退货 17->配送返还 18 ->商城退货
    "sevenBankType":None, # 8种银行流水款项类型 0 -> 全部 1->汇押货款 2-> 1:3押货款退款申请 3-> 手工退押货款 4-> 手工增押货款 5-> 转销售 6-> 钱包款与押货款互转 7-> 其他 、8->押货保证金转移
    "tenType":None, # 11种底层交易类型 0 -> 全部 1->汇押货款、2-> 退押货款、3-> 信誉额、12-> 其他、13-> 产品调价、14-> 押货使用、15-> 押货退货、16-> 押货调整、17-> 配送返还、18-> 商城退货, 19->押货保证金转移
    "bizNo":None, # 业务单号
    "pageNum":1,
    "pageSize":10,
    "startMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04"
    "endMonth": time.strftime("%Y-%m",time.localtime(time.time())), #"2022-04" 结束月份期间(yyyy-MM)
}

def _mgmt_inventory_mortgageAmount_mortgageAmountChangePageList(data=data, access_token=access_token):
    """
    服务中心账款管理 -- 押货余额详情(详情分页列表)
    /mgmt/inventory/mortgageAmount/mortgageAmountChangePageList
    """

    url = f"{BASE_URL}/mgmt/inventory/mortgageAmount/mortgageAmountChangePageList"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
