# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.getcwd())

from base.read_data import read_yaml_data



import time

import pytest

import page
from base.init_driver import get_driver
from page.navigation_page import NavigationPage


def get_test_login_data():
    data_list = []
    login_data = read_yaml_data("login_data.yaml")
    for i in login_data.keys():
        usename = login_data.get(i).get("usename")
        password = login_data.get(i).get("password")
        data_list.append((usename, password))
    return data_list

class TestAolai:
    def setup_class(self):
        self.driver = get_driver(page.aolai_app_package,page.aolai_app_activity)
        self.navigation_page = NavigationPage(self.driver)

    def teardown_class(self):
        time.sleep(1)
        self.driver.quit()


    # 测试登录模块
    @pytest.mark.parametrize("username,password",get_test_login_data())
    def test_login(self,username,password):
        time.sleep(3)
        # 点击我的按钮
        self.navigation_page.get_home_page_obj().click_btn_mine()
        time.sleep(2)
        # 点击已有账号,去登陆
        self.navigation_page.get_regist_page_obj().click_btn_have_ID_goto_login()
        time.sleep(2)
        # 输入账号,密码,点击登录
        self.navigation_page.get_login_page_obj().login_page_in()
        # 4.获取toast的内容 通过xpath定位
        toast_msg = self.navigation_page.get_login_page_obj().find_element(page.aolai_toast_pwd_error).text
        print(toast_msg)