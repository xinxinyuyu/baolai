# -*- coding: utf-8 -*-
import page
from base.base_action import BaseAction


class AddressManagePage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 地址管理页面
    # 点击新增地址按钮
    def click_btn_newaddress(self):
        self.click_element(page.aolai_btn_add_new_address)