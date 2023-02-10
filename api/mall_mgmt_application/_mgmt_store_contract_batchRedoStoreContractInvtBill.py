# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
    "docNos": []
}


def _mgmt_store_contract_batchRedoStoreContractInvtBill(data, access_token=access_token):
    """
    批量撤回对账单电子合同
    /mgmt/store/contract/batchRedoStoreContractInvtBill
    """

    url = f"{BASE_URL}/mgmt/store/contract/batchRedoStoreContractInvtBill"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data["docNos"]

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
