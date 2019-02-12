# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.getcwd())

import time

import pytest
from base.read_data import read_yaml_data
import page
from base.init_driver import get_driver
from page.navigation_page import NavigationPage


def get_test_login_data():
    data_list = []
    login_data = read_yaml_data("login_data.yaml")
    for i in login_data.keys():
        usename = login_data.get(i).get("usename")
        password = login_data.get(i).get("password")
        tag = login_data.get(i).get("tag")
        expect_data = login_data.get(i).get("expect_data")
        data_list.append((usename, password,tag,expect_data))
    return data_list



class TestAolai:
    def setup_class(self):
        self.driver = get_driver(page.aolai_app_package,page.aolai_app_activity)
        self.navigation_page = NavigationPage(self.driver)

    def teardown_class(self):
        time.sleep(1)
        self.driver.quit()


    # def get_test_login_data(self):
    #     data_list = []
    #     login_data = self.read_yaml_data
    #     for i in login_data.keys():
    #         usename = login_data.get(i).get("usename")
    #         password = login_data.get(i).get("password")
    #         return data_list.append((usename,password))




    # 测试登录模块
    @pytest.mark.parametrize("usename,password,tag,expect_data",get_test_login_data())
    def test_login(self,usename,password,tag,expect_data):
        time.sleep(3)
        # 点击我的按钮
        self.navigation_page.get_home_page_obj().click_btn_mine()
        time.sleep(2)
        # 点击已有账号,去登陆
        self.navigation_page.get_regist_page_obj().click_btn_have_ID_goto_login()
        time.sleep(2)
        # 输入账号,密码,点击登录
        self.navigation_page.get_login_page_obj().login_page_in(usename,password)
        time.sleep(2)
        # 4 通过我们自定义的tag 进行预期成功 和失败判断

        if tag == 1:
            try:
                # 点击左上角的设置按钮
                self.navigation_page.get_person_center_page_obj().click_btn_left_setting()
                time.sleep(2)
                # 跳转到设置页面,向上滑动到下面,点击退出登录,弹出框点击确认
                self.navigation_page.get_setting_page_obj().out_login()
            except Exception:
                # 6.当出现异常的情况 实现截图操作
                self.navigation_page.get_setting_page_obj().get_screen()
        else:

            # 7.获取到弹出toast内容 应该是预期结果和实际的结果做对比
            toast_msg = self.navigation_page.get_setting_page_obj().find_element(page.aolai_toast_pwd_error).text
            # 8.判断预期结果和实际结果是否一致
            assert toast_msg == expect_data, self.navigation_page.get_setting_page_obj().get_screen()
            # 9.关闭当前登录页面
            self.navigation_page.get_login_page_obj().click_close_login_page()

