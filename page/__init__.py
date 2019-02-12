# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

# 包名
aolai_app_package = "com.yunmall.lc"
# 启动名
aolai_app_activity = "com.yunmall.ymctoc.ui.activity.MainActivity"


# 定位首页页面元素
# 1.定位我的按钮
aolai_btn_mine = By.ID,"com.yunmall.lc:id/tab_me"

# 定位注册页面元素
# 1.定位已有账号,去登陆
aolai_btn_having_ID_goto_login = By.ID,"com.yunmall.lc:id/textView1"


# 定位登陆页面元素
# 1.定位账号输入框
aolai_input_edit_ID = By.ID,"com.yunmall.lc:id/logon_account_textview"
# 2.定位密码输入框
aolai_input_edit_password = By.ID,"com.yunmall.lc:id/logon_password_textview"
# 3.定位登陆按钮
aolai_btn_login = By.ID,"com.yunmall.lc:id/logon_button"


# 定位个人中心页面元素
# 1.定位设置按钮
aolai_btn_setting = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"

# 定位设置页面元素
# 1.定位退出按钮
aolai_btn_logout = By.ID,"com.yunmall.lc:id/setting_logout"
# 2.定位弹出框的确认按钮
aolai_popup_edit_btn_sure = By.ID,"com.yunmall.lc:id/ymdialog_right_button"
# 3.定位地址管理按钮
aolai_btn_address_manage = By.ID,"com.yunmall.lc:id/setting_address_manage"


# 登录页面
# 定位toast
aolai_toast_pwd_error = By.XPATH,"//*[contains(@text,'密码错误')]"


# 定位地址管理页面元素
# 1.定位新增地址按钮
aolai_btn_add_new_address = By.ID,"com.yunmall.lc:id/address_add_new_btn"


# 定位新增地址页面元素
# 1.定位收件人输入框
aolai_input_receive = By.ID,"com.yunmall.lc:id/address_receipt_name"
# 2.定位手机号输入框
aolai_input_phone_number = By.ID,"com.yunmall.lc:id/address_add_phone"
# 3.定位所在地区选择框
aolai_btn_which_place = By.ID,"com.yunmall.lc:id/address_province"
# 4.比如定位北京市
aolai_btn_beijing_city = By.XPATH,'//*[contains(@text,"北京市")]'
# 5.定位北京市标题按钮
aolai_btn_beijing_title = By.ID,"com.yunmall.lc:id/area_title"
# 6.比如定位东城区
aolai_btn_dongcheng_area = By.XPATH,'//*[contains(@text,"东城区")]'
# 7.定位详细地址的输入框
aolai_input_address_msg = By.ID,"com.yunmall.lc:id/address_detail_addr_info"
# 8.定位邮编输入框
aolai_input_address_post_code = By.ID,"com.yunmall.lc:id/address_post_code"
# 9.定位设为默认地址按钮
aolai_btn_defalt_address = By.ID,"com.yunmall.lc:id/address_default"
# 10.定位保存按钮
aolai_btn_save = By.ID,"com.yunmall.lc:id/button_send"
