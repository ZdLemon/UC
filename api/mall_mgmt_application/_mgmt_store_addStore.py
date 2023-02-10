# coding:utf-8

from util.msg import data_msg
from util.logger import logger
from setting import BASE_URL, TIMEOUT, VERIFY, access_token

import requests


data = {
	"addMemberLeaderAo": {
		"id": "1270780218333983496",
		"memberNo": "800000082172",
		"cardNo": "3000003338",
		"mobile": "13659640006",
		"username": None,
		"email": None,
		"certificatesType": 2,
		"certificatesNo": "4587093",
		"nickname": "3000003338",
		"portraitUrl": None,
		"wechatNickname": None,
		"qqNickname": None,
		"usualLocation": None,
		"channel": 2,
		"channelText": None,
		"defaultDistributionStoreCode": None,
		"createTime": 1645147925000,
		"createTimeText": None,
		"updateTime": 1646797821000,
		"updaterId": "1256132947821634662",
		"updaterName": "test01",
		"memberType": 3,
		"memberStatus": 0,
		"memberStatusText": None,
		"cardStatus": 0,
		"realname": "王杨",
		"gender": None,
		"openCardTime": 1645147925000,
		"firstOrderTime": 1645148351000,
		"lastOrderTime": 1645148351000,
		"lastUpgradeTime": 1646739924000,
		"pv": 356,
		"discount": None,
		"storeCode": "",
		"storeName": None,
		"companyId": "100045866222",
		"handledMemberId": "800001118",
		"handledCardNo": "00001118",
		"handledStoreCode": "902012",
		"distributionCenterType": None,
		"distributionCenterNo": "",
		"distributionCompanyNo": "",
		"distributionCompanyName": "",
		"canLoginMall": 0,
		"canLoginStore": 0,
		"sharerMemberId": "1270780218333983496",
		"changeType": 1,
		"changeTypeText": None,
		"shareMemberCard": None,
		"errorTimes": None,
		"defaultPassword": None,
		"memberLevel": "0",
		"memberLevelMax": None,
		"isFiveStar": 0,
		"contactMobile": "13659640006",
		"openCardId": None,
		"userSource": 1,
		"orderDate": None,
		"cancelDate": None,
		"updateHandledMarker": None,
		"promotionTime": 1645148352000,
		"promotionType": 1,
		"validationOneselfMobileStatus": None,
		"validationOneselfIdcardStatus": None,
		"validationSpouseIdcardStatus": None,
		"openCardMode": None,
		"registerMode": "",
		"openCardModeName": "",
		"registerModeName": None,
		"handledRealname": None,
		"handledMobile": None,
		"handledContactMobile": None,
		"defaultDistributionStoreName": None,
		"haveStore": 1,
		"leaderStoreCode": "942466",
		"leaderStoreCodeName": None,
		"detail": {
			"id": "1270780218333983496",
			"realname": None,
			"mobile": None,
			"email": None,
			"certificatesStartDate": None,
			"certificatesType": None,
			"certificatesNo": None,
			"certificatesEndDate": None,
			"gender": None,
			"birthday": None,
			"company": None,
			"taste": None,
			"education": None,
			"marital": 1,
			"homePhone": None,
			"nationality": None,
			"nation": None,
			"cardEmail": None,
			"livePlace": None,
			"province": None,
			"city": None,
			"district": None,
			"address": None,
			"postcode": None,
			"profession": None,
			"consumeFollow": None,
			"emerContactName": None,
			"emerContactMobile": None,
			"emerContactHomePhone": None,
			"emerContactEmail": None,
			"certificatesPositiveUrl": None,
			"certificatesReverseUrl": None,
			"opencardPositiveUrl": None,
			"opencardReverseUrl": None,
			"spouseMemberId": None,
			"spouseOrNot": 0,
			"spouseGender": None,
			"spouseMobile": None,
			"spouseRealname": None,
			"spouseBirthday": None,
			"spouseEducation": None,
			"spouseMarital": None,
			"spouseCertificatesType": None,
			"spouseCertificatesNo": None,
			"spouseCertificatesStartDate": None,
			"spouseCertificatesEndDate": None,
			"spouseProvince": None,
			"spouseCity": None,
			"spouseDistrict": None,
			"spouseAddress": None,
			"spouseHomePhone": None,
			"spouseCardEmail": None,
			"spousePostcode": None,
			"spouseLivePlace": None,
			"spouseNation": None,
			"spouseProfession": None,
			"spouseConsumeFollow": None,
			"spouseCertificatesPositiveUrl": None,
			"spouseCertificatesReverseUrl": None,
			"createTime": 1645147925000,
			"updateTime": 1645147925000,
			"provinceName": None,
			"cityName": None,
			"districtName": None,
			"spouseProvinceName": None,
			"spouseCityName": None,
			"spouseDistrictName": None,
			"spouseIsBind": None,
			"spouseMobileBindCardNo": None
		},
		"mobiles": None,
		"handledLeaderStoreCode": None,
		"type": None,
		"memberStatusUpdateTime": None,
		"qq": None,
		"wechat": None,
		"updateHandled": None,
		"updateSpouse": None,
		"del": None,
		"discountPermission": None,
		"businessMode": None,
		"validationStatusList": None,
		"companyCode": "02000",
		"certificatesPositiveUrl": "",
		"certificatesReverseUrl": ""
	},
	"storeVO": {
		"city": "",
		"code": "",
		"companyCode": "02000",
		"isMainShop": 1,
		"leaderNo": "3000003338",
		"name": "王杨服务中心二号店",
		"openDate": "",
		"permission": "1,2,3,4,5",
		"discountPermission": "",
		"businessMode": 1,
		"isHighPriority": 2,
		"province": "",
		"ratifyDate": "2022-03-08T16:00:00.000Z",
		"remarks": "王杨开的第二家店",
		"shopStatus": "",
		"shopkeeperNo": "",
		"storeId": "",
		"zipCode": "",
		"isSignContract": "",
		"isSignAgreement": "",
		"decorationInfo": "{\"totalArea\":\"\",\"businessArea\":\"\",\"leaseTerm\":\"\",\"monthlyRent\":\"\",\"shopLength\":\"\",\"businessFloorHeight\":\"\",\"shopWidth\":\"\",\"signLength\":\"\",\"signWidth\":\"\",\"propertyType\":\"\",\"isSign\":\"\",\"isLed\":\"\"}",
		"deliveryInfo": "{\"person\":\"王杨\",\"phoneNum\":\"13659640006\",\"address\":\"琶洲新村11号\",\"receiptSeal\":\"\",\"contactProvinceName\":\"广东省\",\"contactProvinceCode\":\"440000000000\",\"contactCityName\":\"广州市\",\"contactCityCode\":\"440100000000\",\"contactAreaName\":\"海珠区\",\"contactAreaCode\":\"440105000000\",\"contactStreetName\":\"琶洲街道\",\"contactStreetCode\":\"440105015000\",\"detailAddress\":\"琶洲新村11号\",\"deliveryProvinceName\":\"广东省\",\"deliveryProvinceCode\":\"440000000000\",\"deliveryCityName\":\"广州市\",\"deliveryCityCode\":\"440100000000\",\"deliveryAreaName\":\"海珠区\",\"deliveryAreaCode\":\"440105000000\",\"deliveryStreetName\":\"琶洲街道\",\"deliveryStreetCode\":\"440105015000\"}",
		"addressInfo": "{\"detailAddress\":\"\",\"contactAddress\":\"\"}",
		"extraInfo": "{\"subShopName\":\"\",\"unContactReason\":\"\",\"phone1\":\"\",\"email1\":\"\",\"phone2\":\"\",\"email2\":\"\",\"legalPerson\":\"\",\"legalInfo\":\"\",\"originalStore\":\"\",\"guaranteeName1\":\"\",\"guaranteeCard1\":\"\",\"guaranteeCenter1\":\"\",\"isTransProvincial\":\"\",\"guaranteeCard2\":\"\",\"guaranteeName2\":\"\",\"guaranteeCenter2\":\"\",\"cancelTime\":\"\",\"frozenTime\":\"\",\"frozenReason\":\"\",\"contractStartDate\":\"\",\"code\":\"942466\"}",
		"isSettledAccount": 2,
		"shopType": 1,
		"provinceName": "广东省",
		"provinceCode": "440000000000",
		"cityName": "广州市",
		"cityCode": "440100000000",
		"areaName": "海珠区",
		"areaCode": "440105000000",
		"streetName": "琶洲街道",
		"streetCode": "440105015000",
		"contactSite": ["440000000000", "440100000000", "440105000000", "440105015000"],
		"receiveGoodsSite": ["440000000000", "440100000000", "440105000000", "440105015000"],
		"level": 2,
		"companyName": "广东分公司"
	},
	"credentialVO1": {
		"certificateDate": "",
		"credentialType": "",
		"expiryDate": "",
		"picUrls": "",
		"storeCode": "",
		"info": "{\"certificateName\":\"\",\"certificateCode\":\"\",\"certificatePerson\":\"\",\"isFive\":\"\",\"operatorName\":\"\",\"operatorType\":\"\",\"socialCreditCode\":\"\",\"composition\":\"\",\"identificationCode\":\"\",\"certificationAuthority\":\"\",\"businessPlace\":\"\",\"isSale\":\"\",\"businessScope\":\"\"}"
	},
	"credentialVO2": {
		"certificateDate": "",
		"credentialType": "",
		"expiryDate": "",
		"info": "{\"picUrls\":\"\",\"storeCode\":\"\",\"code\":\"\",\"certificationAuthority\":\"\",\"businessScope\":\"\"}"
	},
	"credentialVO3": {
		"certificateDate": "",
		"credentialType": "",
		"expiryDate": "",
		"info": "{\"picUrls\":\"\",\"storeCode\":\"\",\"isFoodBusinessLicense\":\"\",\"licenseKey\":\"\",\"certificationAuthority\":\"\",\"businessScope\":\"\"}"
	}
}


def _mgmt_store_addStore(data, access_token=access_token):
    """
    添加服务中心
    /mgmt/store/addStore
    """

    url = f"{BASE_URL}/mgmt/store/addStore"
    headers = {
        "Authorization": f"bearer {access_token}", 
        "content-type": "application/json;charset=UTF-8"
    }
    data = data

    with requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT, verify=VERIFY) as r:    
        logger.debug(data_msg(r, data))     
        return r
