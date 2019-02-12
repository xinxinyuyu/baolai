# -*- coding: utf-8 -*-
from base.base_action import BaseAction
from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.regist_page import RegistPage
from page.setting_page import SettingPage


class NavigationPage(BaseAction):
    def __init__(self,driver):
        self.driver = driver
    # 导航页面

    # 获取首页面的实例
    def get_home_page_obj(self):
        return HomePage(self.driver)

    # 获取注册页面的实例
    def get_regist_page_obj(self):
        return RegistPage(self.driver)

    # 获取登录页面的实例
    def get_login_page_obj(self):
        return LoginPage(self.driver)

    # 获取个人中心页面的实例
    def get_person_center_page_obj(self):
        return PersonCenterPage(self.driver)

    # 获取设置页面的实例
    def get_setting_page_obj(self):
        return SettingPage(self.driver)