import time
from email import message

from selenium.webdriver.common.by import By

link = "https://spb.restate.ru/complex/lermontovskiy-54-5255.html"


class TestMainPage:
    def test_find_button(self, browser):
        browser.get(link)
        browser.implicitly_wait(5)
        button = browser.find_element(By.ID, "recall_tr")

    def test_find_button_open_popup(self, browser):
        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element(By.ID, "recall_tr")
        button = browser.find_element(By.ID, "recall_tr")
        button.click()
        browser.find_element(By.ID, "recallPopup2019")
