import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import re
import logging

# log = logging.getLogger(__name__)
# log.setLevel('INFO')


def get_urls():
    urls = re.findall(r'[>"]\s*((?:https?:\/\/|ftps?:\/\/|www\.)[^<"]*?)\s*["<]',
                      open('/Users/alexwell/Downloads/spb.restate.ru.xml').read())
    return urls


class TestMainPage:
    @pytest.mark.parametrize('link', get_urls())
    def test_find_button(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(7)
        try:
            button = browser.find_element(By.ID, "recall_tr")
        except NoSuchElementException as e:
            print("error test1 with link: ", link)
            assert False

        button.click()
        try:
            browser.find_element(By.ID, "recallPopup2019")
            # message = browser.find_element_by_class_name("rfp-t2019__logo-wrp")
            # browser.implicitly_wait(3)
        except NoSuchElementException as e:
            print("error test2 with link: ", link)
            assert False

    if __name__ == "__main__":
        test_find_button()
