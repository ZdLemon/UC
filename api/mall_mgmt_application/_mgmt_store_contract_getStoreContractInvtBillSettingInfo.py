# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


params = {
    "signType" : 2,  # 对账单签署类型，1/1:3库存对账单，2/85%库存对账单，3/85%账款对账单
}


def _mgmt_store_contract_getStoreContractInvtBillSettingInfo(params=params, access_token=access_token):
    """
    获取公司签署人信息
    /mgmt/store/contract/getStoreContractInvtBillSettingInfo
    """

    url = f"{BASE_URL}/mgmt/store/contract/getStoreContractInvtBillSettingInfo"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
