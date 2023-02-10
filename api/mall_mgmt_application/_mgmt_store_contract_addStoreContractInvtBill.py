# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, USERNAME

import requests
import datetime


data = {
    "signStartDate": (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"), # 签署开始日期，格式：yyyy-MM-dd 明天
    "billType":1, # 对账单类型，1/实时，2/月结
    "storeCode":"902088",
    "companyCustomerId":"d3da86ac083349a6ba6c03f75bf61119", # 公司签署人法大大客户编号(必填)
    "companySignPerson":"1506033", # 公司签署人OA工号(必填)
    "currentOperatorName": USERNAME, # 当前操作人名称
    "signType":2 # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
}


def _mgmt_store_contract_addStoreContractInvtBill(data=data, access_token=access_token):
    """
    添加库存对账单电子合同批量任务
    /mgmt/store/contract/addStoreContractInvtBill
    """

    url = f"{BASE_URL}/mgmt/store/contract/addStoreContractInvtBill"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
