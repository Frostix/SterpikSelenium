from selenium import webdriver
from math import sin, log
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(log(abs(12*sin(x))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome("C:\Chromedriver\chromedriver")
browser.get(link)


button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR"))
button = browser.find_element_by_id("book")        
button.click()


x = browser.find_element_by_id("input_value")
x = int(x.text)
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)

button = browser.find_element_by_id("solve")
button.click()