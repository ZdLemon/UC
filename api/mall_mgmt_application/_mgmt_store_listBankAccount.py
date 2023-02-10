# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time


params = {
    "opType": None, # 操作类型 1新增 2修改 3作废
    "verifyStatus": None, # 审核状态 3待审核, 不选则是全部
    "pageNum": 1, 
    "pageSize": 10,
    "storeCode": None, # 服务中心编号
    "isUsed": None, # 作废标示 1生效 2作废
    "leaderCardNo": None, # 总店负责人卡号
    "isSigned": None # 是否已签约，1/是，2/否
}


def _mgmt_store_listBankAccount(params=params, access_token=access_token):
    """
    银行账号列表
    /mgmt/store/listBankAccount
    """

    url = f"{BASE_URL}/mgmt/store/listBankAccount"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
    
