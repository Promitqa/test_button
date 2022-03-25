from os import link

from testwork.pages.conftest import browser
from testwork.pages.main_page import MainPage


def test_find_button(browser):
    link = 'https://spb.restate.ru/complex/cvetnoy-gorod-341.html'
    page = MainPage(browser, link)
    page.open()
    page.find_element_button()


def test_guest_should_see_popup(browser):
    link = 'https: // spb.restate.ru / complex / cvetnoy - gorod - 341.html'
    page = MainPage(browser, link)
    page.open()
    page.should_be_popup()
