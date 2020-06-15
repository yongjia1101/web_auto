import pytest
from pages.login_page import LoginPage
from selenium import webdriver


@pytest.fixture(scope="session")
def login_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 先登录
    web = LoginPage(driver)
    web.login()
    return driver



