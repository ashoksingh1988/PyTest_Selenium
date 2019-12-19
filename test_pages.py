from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .test_base import Page
from .test_locators import *
#from users import users
import pytest
from selenium.webdriver.support.ui import WebDriverWait


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes
@pytest.mark.usefixtures("driver_init")
class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocatars
        super().__init__(driver)  # Python3 version

        # super(TestBrowser,self).__init__()

    def search_item(self, item):
        return self.find_element(*self.locator.SEARCHLIST).send_keys(item)

    def click_element(self):
        self.find_element(*self.locator.SEARCH).click

    def enter_item(self):
        return self.find_element(*self.locator.SEARCHLIST).send_keys(Keys.ENTER)

    def text_element(self):
        return self.find_element(*self.locator.SEARCH).text
            # timeout =3
            # return self.find_element(*self.locator.SEARCH).text
            # try:
            # element_present = EC.presence_of_element_located((self.find_element(*self.locator.SEARCH)))
            # WebDriverWait(self.driver, timeout).until(element_present)

            #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
            #                                          ((self.driver.find_element(self.MainPageLocatars.SEARCH))))
            #
            # except TimeoutException:
            #     print
            #     "Timed out waiting for page to load"
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.find_element(*self.locator.SEARCH)))
            # WebDriverWait(self.driver, 10).until(element)
            # return element.text

    def get_url(self):
        return self.driver.current_url

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def action_click_options(self):
      self.find_element(*self.locator.HealthIT).click()

    def action_click_options1(self):
      self.find_element(*self.locator.Finance).click()

    def action_click_options2(self):
      self.find_element(*self.locator.Menu).click()

    def search_item1(self, item):
        return self.find_element(*self.locator.EmailInput).send_keys(item)

    def action_click_options3(self):
      self.find_element(*self.locator.signup).click()