import time
import unittest

from selenium import webdriver


def first_test():
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("https://spb.restate.ru/complex/landrin-loft-5222.html")
    button = driver.find_element_by_id("recall_tr")

    if button is None:
        print("Элемент не найден")
    else:
        print('Элемент найден')
