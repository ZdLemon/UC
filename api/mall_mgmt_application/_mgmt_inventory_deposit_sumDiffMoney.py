# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests
import time


data = {
	"storeCode": store_85, # 服务中心编号
	"mortgageOrderNoOrBusinessNo": None, # 押货单号or流水号
	"pageNum": 1,
	"pageSize": 10,
	"reportType": [], # 报表字段 1 ->本期汇/退款 2->本期押货/退押 3-> 交付差额转入
	"moneyType": [], # 款项类型 1->汇押货款、3->其他、7->手工增加押货款、8->手工退押货款、9->押货保证金转移
	"dealType": [], # 交易类型 1->汇押货款、2->退押货款、3->其他、4->押货使用 5->押货退货、6->交付月结差额转入 9->押货保证金转移
	"startDay": f"{time.strftime('%Y-%m',time.localtime(time.time()))}-01", # 当月第一天, 交易日期2022-04-01
	"endDay": time.strftime("%Y-%m-%d",time.localtime(time.time())) # 当月当天,交易开始月份2022-04-04
}


def _mgmt_inventory_deposit_sumDiffMoney(data=data, access_token=access_token):
    """
    85折账款管理 -- 交易金额合计--保证金详情金额合计
    /mgmt/inventory/deposit/sumDiffMoney
    """

    url = f"{BASE_URL}/mgmt/inventory/deposit/sumDiffMoney"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
