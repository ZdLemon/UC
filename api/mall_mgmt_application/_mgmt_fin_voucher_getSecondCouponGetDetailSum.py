# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time
import calendar


data = {
	"cardNo": "", # 会员卡号
	"memberType": None, # 顾客类型
	"sourceOrderNo": None, # 来源订单号
	"getType": None, # 交易类型，1：购物获得；2：月结更新
	"sourceStoreCode": None, # 服务中心编号
	"couponStatus": None, # 券状态
	"pageNum": 1,
	"pageSize": 10,
	"getStartTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # 获券开始时间-yyyy-MM-dd HH:mm:ss
	"getEndTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # 获券结束时间-yyyy-MM-dd HH:mm:ss
	"transMonthStart": None, # 交易月份开始YYYYMM，运营后台使用
	"transMonthEnd": None # 交易月份结束YYYYMM，运营后台使用
}

def _mgmt_fin_voucher_getSecondCouponGetDetailSum(data=data, access_token=access_token):
    """
    秒返券获券合计
    /mgmt/fin/voucher/getSecondCouponGetDetailSum
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/getSecondCouponGetDetailSum"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
