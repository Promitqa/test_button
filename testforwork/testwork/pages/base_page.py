from pip._internal.utils import urls
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser):
        self.browser = browser
        self.url = urls

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, browser, url):
        try:
            self.browser.find_element(browser, url)
        except NoSuchElementException:
            return False
        return True
