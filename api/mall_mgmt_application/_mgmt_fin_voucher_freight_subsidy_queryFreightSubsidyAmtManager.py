# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time
import calendar


data = {
	"cardNo": None,
	"mobile": None,
	"memberType": None, # 会员类别：1->普通顾客；2->优惠顾客；3->云商；4->微店（云+）；5->店员；6->子账号
	"shopCode": None,
	"subsidyReason": None, # 运费补贴原因 1:押货退货 2:押货换货 3:展业包订购单退货 4:展业包订购单换货 5:顾客订单退货 6:顾客订单换货
	"freightCouponStatus": None, # 运费补贴券状态 1:已使用 2:未使用 3:占用中 4:已失效
	"pageNum": 1,
	"pageSize": 10,
	"startTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-01 00:00:00', # yyyy-MM-dd HH:mm:ss"2022-05-01 00:00:00"
	"endTime": f'{time.strftime("%Y-%m",time.localtime(time.time()))}-{calendar.monthrange(time.localtime(time.time()).tm_year,time.localtime(time.time()).tm_mon)[1]} 23:59:59', # yyyy-MM-dd HH:mm:ss，当月最后一天
}


def _mgmt_fin_voucher_freight_subsidy_queryFreightSubsidyAmtManager(data=data, access_token=access_token):
    """
    运费费补贴券金额统计（商城后台）
    /mgmt/fin/voucher/freight/subsidy/queryFreightSubsidyAmtManager
    """

    url = f"{BASE_URL}/mgmt/fin/voucher/freight/subsidy/queryFreightSubsidyAmtManager"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
