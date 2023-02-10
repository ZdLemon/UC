# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"transTime": time.strftime('%Y-%m',time.localtime(time.time())), # 月份
	"companyCode": "34000", # 分公司编号不能为空
	"timerange": [],
	"cardNo": None, # 会员卡号
	"mobile": None, # 普客手机号
	"memberTypeList": [], # 顾客类型 1：普通顾客；2：优惠顾客；3：云商；4：微店
	"transType": None, # 账款类型, 参数说明：1：充值；2：购货转入；6：提现；7：原路退款；9:还欠款；10；补银行流水；11：手工退款；12：押货款与钱包互转；13：其他；16：定金转入
	"autoType": None, # 自动/手工，参数说明 1：自动；2：手工；
	"pageNum": 1,
	"pageSize": 10,
	"startTime": None, # 到账开始时间
	"endTime": None # 到账结束时间
}


def _mgmt_fin_wallet_bill_queryFinWalletCompanyAccountTrans(data=data, access_token=access_token):
    """
    查询分公司银行流水(商城后台)
    /mgmt/fin/wallet/bill/queryFinWalletCompanyAccountTrans
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/bill/queryFinWalletCompanyAccountTrans"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
