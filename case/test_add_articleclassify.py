import pytest
from pages.login_page import LoginPage
from pages.articleclassify_page import ArticleClassifyPage
from selenium import webdriver
import allure
import os
from common.connect_mysql import execute_sql
from common.read_yml import get_yaml_data

'''获取测试数据'''
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
test_data_path = os.path.join(project_path, "case", "test_data.yml")
test_data = get_yaml_data(test_data_path)
print(test_data)


@pytest.fixture(scope="function")
def delete_date():
    delete_sql = "DELETE FROM hello_articleclassify WHERE n = '技术类' OR n = 'yingwen' OR n = '123456';"
    execute_sql(sql=delete_sql)


@allure.severity("blocker")
@allure.story("编辑文章分类内容")
# @allure.title("编辑文章分类，输入中文，添加成功")
@pytest.mark.parametrize("input_text,expected",
                         test_data["test_add_article_params"],
                         ids=[
                             "编辑文章分类，输入中文，添加成功",
                             "编辑文章分类，输入英文，添加成功",
                             "编辑文章分类，输入数字，添加成功"
                         ]
                         )
def test_add_article(login_fixture, delete_date, input_text, expected):
    """
    用例描述：
        1	点文章分类导航标签 跳转列表页面
        2   点编辑 文章分类按钮，跳转到编辑页面
        3	编辑页面输入，分类名称，如:技术类，test, 123456 可以输入
        4	点保存按钮 保存成功，在列表页显示分类名称：技术类
    """
    driver = login_fixture
    article = ArticleClassifyPage(driver)
    with allure.step("步骤1：点击文章分类按钮"):
        article.click_article_classify()
    with allure.step("步骤2：点击增加文章分类按钮"):
        article.click_add_article_classify()
    with allure.step("步骤3：输入文章分类名称:技术类"):
        article.input_article(input_text)
    with allure.step("步骤4：点击保存按钮"):
        article.click_save_button()

    with allure.step("步骤5：获取页面实际结果，判断是否添加成功"):
        result = article.is_add_success()
        print(result)
    with allure.step("步骤6：断言是否添加成功"):
        assert result == expected


@allure.severity("critical")
@allure.story("编辑文章分类内容")
@allure.title("重复添加文章分类，添加失败")
@pytest.mark.skip()
def test_add_article_2(login_fixture, delete_date):
    """
    用例描述：
        1	文章分类：技术类已添加成功，文章分类再次添加“技术类”
        2	点保存按钮 保存失败，提示已有技术类
    """
    driver = login_fixture
    article = ArticleClassifyPage(driver)
    with allure.step("步骤1：先编辑文章分类-技术类"):
        article.click_article_classify()
        article.click_add_article_classify()
        article.input_article(text='技术类')
        article.click_save_button()
        # 获取结果，完成后返回到列表页面
        result = article.is_add_success()
        print(result)
        assert result

    with allure.step("步骤2：重复添加文章分类-技术类"):
        article.click_add_article_classify()
        article.input_article(text='技术类')
        article.click_save_button()

    # 判断是否添加成功：期望添加失败
    with allure.step("步骤3：获取页面实际结果，判断是否添加成功"):
        result = article.is_add_success()
        print(result)
    with allure.step("步骤4：断言重复添加是否添加成功"):
        assert not result
