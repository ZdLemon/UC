# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token, store_85, productCode

import requests
import time
import calendar


data = {
	"id": "", # id
	"auditRemark": "", # 审核备注
	"auditFileName": "", # 审核附件名称
	"auditResult": "1", # 审核结果 0不通过 1通过
	"auditFileUrl": "", # 审核附件url
	"reasonFirst": "其他原因退货", # 一级原因
	"reasonFirstRemark": "", # 一级原因备注
	"reasonSecond": "特批退货", # 二级原因
	"reasonSecondRemark": "", # 二级原因备注
	"returnInfo": "ujejr",
	"preAuditFileUrl": "",
	"returnAddress": "ujejr"
}


def _mgmt_inventory_dis_mortgage_returnOrder_audit(data=data, access_token=access_token):
    """
    审批
    /mgmt/inventory/dis/mortgage/returnOrder/audit
    """

    url = f"{BASE_URL}/mgmt/inventory/dis/mortgage/returnOrder/audit"
    headers = {"Authorization": f"bearer {access_token}"}
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
