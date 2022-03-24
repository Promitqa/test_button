from testwork.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


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
