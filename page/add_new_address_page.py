# -*- coding: utf-8 -*-
import page
from base.base_action import BaseAction


class AddNewAddressPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 新增地址页面
    def new_address(self):
        # 输入收件人
        self.input_edit_content(page.aolai_input_receive)
        # 输入手机号
        self.input_edit_content(page.aolai_input_phone_number)
        # 点击所在地区按钮
        self.click_element(page.aolai_btn_which_place)
        # 点击北京市按钮
        self.click_element(page.aolai_btn_beijing_city)
        # 点击北京市标题的按钮
        self.click_element(page.aolai_btn_beijing_title)
        # 点击东城区按钮
        self.click_element(page.aolai_btn_dongcheng_area)
        # 输入详细地址
        self.input_edit_content(page.aolai_input_address_msg)
        # 点击保存按钮
        self.click_element(page.aolai_btn_save)


    # 邮编可选项
    def address_post_code(self):
        self.input_edit_content(page.aolai_input_address_post_code)
    # 设为默认地址
    def address_defalt(self):
        self.click_element(page.aolai_btn_defalt_address)