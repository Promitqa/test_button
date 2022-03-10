from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/.../.../chromedriver.exe')
driver.get("https://www.saucedemo.com/")
input_username = driver.find_element_by_id("user-name")
if input_username is None:
   print("Элемент не найден")
else:
   print("Элемент найден")