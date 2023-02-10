# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

from urllib.parse import urlencode
import requests


data = {
    "docNo": "", # 合同编号
}


def _mgmt_store_contract_signContractInvtBillOffline(data=data, access_token=access_token):
    """
    线下签署对账单电子合同
    /mgmt/store/contract/signContractInvtBillOffline
    """

    url = f"{BASE_URL}/mgmt/store/contract/signContractInvtBillOffline"
    headers = {"Authorization": f"bearer {access_token}", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    data = urlencode(data) # application/x-www-form-urlencoded传参需要特殊处理

    with requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
