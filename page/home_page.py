# -*- coding: utf-8 -*-
import page
from base.base_action import BaseAction


class HomePage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    # 首页页面
    # 点击我的按钮
    def click_btn_mine(self):
        self.click_element(page.aolai_btn_mine)
