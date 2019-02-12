# -*- coding: utf-8 -*-
import page
from base.base_action import BaseAction


class PersonCenterPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 个人中心页面
    # 点击左上角的设置按钮
    def click_btn_left_setting(self):
        self.click_element(page.aolai_btn_setting)
