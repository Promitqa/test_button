import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import re
import logging


log = logging.getLogger(__name__)
log.setLevel('INFO')


def get_urls():
    urls = re.findall(r'[>"]\s*((?:https?:\/\/|ftps?:\/\/|www\.)[^<"]*?)\s*["<]',
                      open('/Users/alexwell/Downloads/spb.restate.ru.xml').read())
    return urls


@pytest.mark.parametrize('link', get_urls())
class TestMainPage:

    def test_find_button(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(3)
        button = browser.find_element(By.ID, "recall_tr")
        button.click()


        input1 = browser.find_element(By.CLASS_NAME, 'rfp-t2019__input-text')
        if input1.is_displayed():
            input1.send_keys("111 111 11 11")

#
#     if __name__ == "__main__":
#         test_find_button()
