from common.base import Base


class ArticleClassifyPage(Base):
    # 文章分类 定位到2个
    loc1 = ("xpath", '//*[@href="/xadmin/hello/articleclassify/"]')
    # 增加文章分类
    loc2 = ("xpath", '//*[@id="content-block"]/div[1]/div[2]/div/a')
    # 分类输入框
    loc3 = ("xpath", '//*[@id="id_n"]')
    # 保存按钮
    loc4 = ("xpath", '//*[@id="articleclassify_form"]/div[2]/button/i')
    # 判断添加成功
    loc5 = ("xpath", '//*[@id="content-block"]/div[2]')

    def click_article_classify(self):
        '''点击文章分类按钮'''
        # self.click(self.loc1)
        self.finds(self.loc1)[0].click()

    def click_add_article_classify(self):
        '''点击增加文章分类按钮'''
        self.click(self.loc2)

    def input_article(self, text='技术类'):
        '''输入文章分类名称'''
        self.send(self.loc3, text)

    def click_save_button(self):
        '''点击保存按钮'''
        self.click(self.loc4)

    def is_add_success(self, expect_text='添加成功'):
        text = self.get_text(self.loc5)
        print("获取到元素的文本内容：%s" % text)
        return expect_text in text

# if __name__ == '__main__':
#     from pages.login_page import LoginPage
#     from selenium import webdriver
#     from common.base import Base
#
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     # 先登录
#     web = LoginPage(driver)
#     web.login()
#
#     article = ArticleClassifyPage(driver)
#     # 点击文章分类按钮
#     article.click_article_classify()
#     # 点击增加文章分类按钮
#     article.click_add_article_classify()
#     # 输入文章分类名称
#     article.input_article(text='技术类')
#     # 点击保存按钮
#     article.click_save_button()
#     # 判断添加成功
#     result = article.is_add_success()
#     print(result)

