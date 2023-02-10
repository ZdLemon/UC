# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"cardNo": None, # 会员卡号
	"mobile": None, # 手机号码
	"realname": None, # 顾客姓名
	"companyCode": None, # 分公司编号
	"timerange": None, # 申请提现时间
	"withdrawStatus": 0, # 提现状态,0:全部，1：待审核；2：待受理；4：汇款成功；5：汇款失败；6：已撤销
	"pageNum": 1,
	"pageSize": 10
}

def _mgmt_fin_wallet_getWalletWithdrawTotalAmt(data=data, access_token=access_token):
    """
    余额提现审批-总计
    /mgmt/fin/wallet/getWalletWithdrawTotalAmt
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getWalletWithdrawTotalAmt"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
