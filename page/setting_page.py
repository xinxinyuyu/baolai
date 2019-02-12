# -*- coding: utf-8 -*-
import time

import page
from base.base_action import BaseAction
class SettingPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 设置页面

    # 退出登录
    def out_login(self):
        # 向上滑动
        self.swipe_screen(1)
        time.sleep(2)
        # 点击退出按钮
        self.click_element(page.aolai_btn_logout)
        # 弹出框点击确认
        self.click_element(page.aolai_popup_edit_btn_sure)

    # 进入地址管理
    def in_btn_address_manage(self):
        # 点击地址管理
        self.click_element(page.aolai_btn_address_manage)
