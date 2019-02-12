# -*- coding: utf-8 -*-
import page
from base.base_action import BaseAction
class LoginPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 在登录页面

    def login_page_in(self,usename,password):
        # 1.输入账号
        self.input_edit_content(page.aolai_input_edit_ID,usename)

        # 2.输入密码
        self.input_edit_content(page.aolai_input_edit_password,password)
        # 3.点击登录按钮
        self.click_element(page.aolai_btn_login)