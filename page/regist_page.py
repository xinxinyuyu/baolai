# -*- coding: utf-8 -*-
import page
from base.base_action import BaseAction
class RegistPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 在注册页面点击已有账号,去登陆按钮
    def click_btn_have_ID_goto_login(self):
        self.click_element(page.aolai_btn_having_ID_goto_login)



