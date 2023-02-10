# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests
import time


data = {
	"id": "", # 押货退货单id
	"auditRemarks": "我审核备注哦啦啦啦", # 审核备注
	"auditFileName": "", # 审核附件名称
	"auditStatus": 1, # 审核结果 0不通过 1通过
	"auditFileUrl": "", # 审核附件url
	"reasonFirst": "其他原因退货", # 一级原因
	"reasonFirstRemarks": "我就是想退货，你敢不同意吗", # 一级原因备注
	"reasonSecond": "特批退货", # 二级原因
	"reasonSecondRemarks": "算了，这次就允许你退货吧", # 二级原因备注
	"returnInfo": "", # 退回地址信息
	"preAuditFileUrl": ""
}


def _mgmt_inventory_returnOrder_auditOrder(data=data, access_token=access_token):
    """
    后台审批押货退货单
    /mgmt/inventory/returnOrder/auditOrder
    """

    url = f"{BASE_URL}/mgmt/inventory/returnOrder/auditOrder"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
