import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # browser = webdriver.Chrome(chrome_options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
