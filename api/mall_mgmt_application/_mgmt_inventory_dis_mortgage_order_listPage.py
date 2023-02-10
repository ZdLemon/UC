# coding:utf-8

from util.msg import params_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85

import requests


params = {
	"pageNum": 1,
	"pageSize": 10,
	"storeCode": "", # 服务中心编号
	"orderSn": "", # 押货单号
	"companyCode": "", # 所属分公司编号
	"modifyFlag": None, # 是否有修改过 0未修改 1已修改
	"orderSource": None, # 押货单来源 1服务中心押货 2运营后台押货
	"orderMark": None, # 标志 1普通押货单 2仅调账不发货 3套装组合押货 4套装拆分押货 5 1:3转库存押货
	"payType": None, # 支付方式 1保证金 2工行签约代扣 3建行签约代扣 4工行签约代扣+保证金 5建行签约代扣+保证金
	"beginTime": "", # 开始提交时间
	"endTime": "", # 结束提交时间
	"beginMortgageTime": "", # 开始押货时间
	"endMortgageTime": "", # 结束押货时间
	"orderStatus": None, # 押货单状态 1待审核 2待支付 3待发货 4部分发货 5已完成 6已取消
	"customFlag": 0,
	"isTrafficControl": None # 是否处于交通管制 0否 1是
}

def _mgmt_inventory_dis_mortgage_order_listPage(params=params, access_token=access_token):
    """
    押货单列表查询
    /mgmt/inventory/dis/mortgage/order/listPage
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/order/listPage"
    headers = {"Authorization": f"bearer {access_token}"}
    params = params

    with requests.get(url=url, headers=headers, params=params, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(params_msg(r, params))     
        return r
