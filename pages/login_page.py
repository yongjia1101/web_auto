from common.base import Base

url = "http://49.235.92.12:8020/xadmin/"


class LoginPage(Base):
    loc1 = ("id", "id_username")
    loc2 = ("xpath", '//*[@id="id_password"]')
    loc3 = ("xpath", '//button[text()="登录"]')

    # 判断元素
    loc4 = ("xpath", '//*[text()="后台页面"]')

    def input_username(self, text="admin"):
        '''输入用户名'''
        self.send(self.loc1, text)

    def input_password(self, text="yoyo123456"):
        '''输入密码'''
        self.send(self.loc2, text)

    def click_button(self):
        '''点击登录按钮'''
        self.click(self.loc3)

    def login(self, user="admin", password="yoyo123456"):
        '''登录'''
        self.driver.get(url)
        self.input_username(user)
        self.input_password(password)
        self.click_button()

    def is_login_success(self):
        '''判断是否登录成功'''
        return self.is_element_exist(self.loc4)

# if __name__ == '__main__':
#     from selenium import webdriver
#     from common.base import Base
#     driver = webdriver.Chrome()
#     # driver.get(url)
#     web = LoginPage(driver)
#     web.login()
#     result = web.is_login_success()
#     print("登录结果：", result)
#     assert result
#     driver.quit()

