# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"auditRemark": "", # 审批备注
	"remittanceRemark": "提现", # 汇款备注
	"status": 2, # 审核状态-用于审核，撤销：2：通过；6：不通过；6：撤销
	"transferStatus": 4, # 汇款状态-用于汇款成功，汇款失败：4：汇款成功，5：汇款失败。
	"walletWithdrawId": "89" # 余额提现id
}

def _mgmt_fin_wallet_auditTransferWithdraw(data=data, access_token=access_token):
    """
    余额提现审批-汇款
    /mgmt/fin/wallet/auditTransferWithdraw
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/auditTransferWithdraw"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
