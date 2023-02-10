# pytest 接口测试约定

#### 具体如图（data/doc/ **）

## 接口API管理

- 遵照开发的微服务模块结构，一个微服务一个文件夹
- api文件名为其url路径（反斜杠转成下划线）如：_mobile_order_before_thrivingHistoryList.py
- api文件撰写如图

## 用例管理

- 按产品端划分单独用例文件夹，如完美运营后台：testcases，商城pc端：pc_testcases
- 具体用例分层组织按功能模块分，文件夹名称必须用中文（allure功能视角）
- 用例文件名为: test+api文件名，如：test_mobile_order_before_thrivingHistoryList.py
- 一个接口的所有用例都必须放在一个文件里面（通过类+函数方法组织）
- 用例使用allure装饰器匹配报告结构
  - @allure.feature("mall_mgmt_application") -- 所属微服务，放在类上
  - @allure.story("/mgmt/store/checkBusinessAddressIsExist") -- 所属接口，放在类上
  - @allure.severity(P2) --用例级别，放在函数用例上
  - @allure.title("检查经营地址是否存在-成功路径: 经营地址不重复时返回None检查") --用例标题，放在函数用例上
  - @allure.step("我是测试步骤一") --用例步骤，放在函数用例里面的测试步骤step上

## ssh配置

- 公钥密钥
- 全局安全配置-Git Host Key Verification Configuration-Accept first connection