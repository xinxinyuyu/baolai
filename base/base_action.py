"""
类里面包含公共的操作 比如查找元素 点击元素 向输入框里面输入内容...
"""
import time
class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    # 这个方法就是查找元素的方法
    def find_element(self, loc):
        time.sleep(1) #找元素之前等一会
        # self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])

    #定位一组元素
    # def find_elements(self,loc):
    #     time.sleep(1)
    #     return self.driver.find_elements(loc[0],loc[1])

    #点击元素的方法
    def click_element(self,loc):
        self.find_element(loc).click()

    #向输入框里面输入内容
    def input_edit_content(self,loc,content):
        input_element = self.find_element(loc)
        input_element.clear()
        time.sleep(1)
        input_element.send_keys(content)

    # tag 1 2  3 4
    def swipe_screen(self,tag):
        # 获取手机窗口大小
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width")
        height = screen_size.get("height")
        # 向上滚动
        if tag == 1:
            self.driver.swipe(width*0.5, height*0.8, width*0.5, height*0.3, 1000)
        # 向下滚动
        if tag == 2:
            self.driver.swipe(width*0.5, height*0.3, width*0.5, height*0.8, 1000)
        # 向左滚动
        if tag == 3:
            self.driver.swipe(width*0.8, height*0.5, width*0.3, height*0.5, 1000)
        # 向右滚动
        if tag == 4:
            self.driver.swipe(width*0.3, height*0.5, width*0.8, height*0.5, 1000)

        # .截图
        def get_screen(self):
            # 截图名称
            png_name = "./screen/{}.png".format(int(time.time()))
            self.driver.get_screenshot_as_file(png_name)

            # with open("abc.png", "rb") as f:
            # allure.attach("截图名字", f.read(), allure.attach_type.PNG)