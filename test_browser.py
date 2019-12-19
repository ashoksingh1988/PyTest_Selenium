import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .test_pages import MainPage
from .test_locators import MainPageLocatars
from pageobject.pageobject import Locator
from selenium.webdriver.common.by import By
from time import sleep
import pytest


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>
@pytest.fixture(params=["firefox"],scope="class")
def driver_init(request):
    if request.param == "firefox":
        firefox_driver = webdriver.Firefox(executable_path='C:/Users/vijetak/PycharmProjects/Testing/geckodriver-v0.25.0-win64/geckodriver.exe')
        request.cls.driver = firefox_driver
        yield
        firefox_driver.close()


# @pytest.fixture(params=["chrome"],scope="class")
# def driver_init(request):
#     if request.param == "chrome":
#         #web_driver = webdriver.Chrome()
#         chrome_driver = webdriver.Chrome(executable_path='C:/Users/vijetak/PythonPOMSelenium/chromedriver_win32/chromedriver.exe')
#         chrome_driver.maximize_window()
#         request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()
 #   pass

# @pytest.mark.usefixtures("driver_init")
# class BasicTest:
#     pass
#@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@pytest.mark.usefixtures("driver_init")
class TestURL():
    def test_open_url(self):
        self.driver.get("https://www.healthcaredive.com/")
        print(self.driver.title)
        sleep(10)

    def test_menubar_item(self):
        page = MainPage(self.driver)
        result4 = page.action_click_options()
        print("***"+self.driver.title+"***")
        sleep(10)

    def test_inputtext_item(self):
        page = MainPage(self.driver)
        result = page.text_element()
        assert "SEARCH" == result
        result1 = page.click_element()
        result2 = page.search_item("Diabetes")
        result3 = page.enter_item()
    pass

    def test_manubar_item1(self):
        page = MainPage(self.driver)
        result5 = page.action_click_options1()
        print("###Finance"+self.driver.title+"Finance###")
        sleep(10)

    def test_menubar_item2(self):
        page = MainPage(self.driver)
        #result6 = page.action_click_options2()
        result7 = page.search_item1("section3testing@gmail.com")
        sleep(5)
        result8 = page.action_click_options3()
        #print("$$$" + self.driver.title + "$$$")

        #Code to list of webelements
        # html_list = self.driver.find_element_by_id("ListMenu")
        # items = html_list.find_elements_by_tag_name("li")
        # for item in items:
        #     text = item.text
        #     print(text)


