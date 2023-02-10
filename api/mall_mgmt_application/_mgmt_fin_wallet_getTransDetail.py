# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
    "walletId":"", # 钱包id
    "reportField":None, # 报表字段 1:本期汇款 2:本期使用 3：本期提现
    "receptionTransType":None, # 前端交易类型 1:汇入,2:退货，3:购货 4:提现,5:退款,6:信用额,7:转款 8:其他 9 预售定金 10 定金返还
    "backstageTransType":None, # 后端交易类型 1:充值 2:购货转入 3:退货转入 4:购货支付 5:提现 6:原路退款 7:信用额增加8:信用额扣减 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转 13:其他 14:定金转入 15:预售定金 16:定金返还
    "orderNo":None, # 订单编号
    "creditEnable":None, # 是否有信用额
    "pageNum":1,
    "pageSize":10,
    "transMonthStart":time.strftime('%Y-%m',time.localtime(time.time())), # 交易月份开始
    "transMonthEnd":time.strftime('%Y-%m',time.localtime(time.time())) # 交易月份结束
}

def _mgmt_fin_wallet_getTransDetail(data=data, access_token=access_token):
    """
    完美钱包管理-交易详情
    /mgmt/fin/wallet/getTransDetail
    """

    url = f"{BASE_URL}/mgmt/fin/wallet/getTransDetail"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r

# 返回值：后端交易类型 1:充值，2：购货转入3:退货转入，6提现，7原路退款，8:购货支付 9:还欠款 10:补银行流水 11:手工退款 12: 押货款与钱包互转，13其他，14信用额增加，15信用额扣减，16:定金转入，17预售定金，18定金返还
# 返回值：1,2,9,10,16汇入 3退货 6提现 7,11退款 8购货 12转款 13其他 14,15信用额 17预售定金 18定金返还