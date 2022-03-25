from selenium_env.bin import pytest
from testwork.pages.base_page import BasePage
from selenium.webdriver.common.by import By

import re


# def get_urls():
#     urls = re.findall(r'[>"]\s*((?:https?:\/\/|ftps?:\/\/|www\.)[^<"]*?)\s*["<]',
#                       open('/Users/alexwell/Downloads/spb.restate.ru.xml').read())
#     return urls
#
#
# @pytest.mark.parametrize('link', get_urls())
class MainPage(BasePage):
    def find_element_button(self):
        button = self.browser.find_element(By.ID, "recall_tr")
        button.click()

    def find_element_button(self):
        assert self.is_element_present(By.ID, "recall_tr"), "Not found button"

    def should_be_popup(self):
        self.browser.find_element(By.CLASS_NAME, "rfp-t2019__input-text")

    def should_be_popup(self):
        assert self.is_element_present(By.CLASS_NAME, "rfp-t2019__input-text"), "Not found popup"
