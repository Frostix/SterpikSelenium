from selenium import webdriver
from math import sin, log

def calc(x):
  return str(log(abs(12*sin(x))))


browser = webdriver.Chrome("C:\Chromedriver\chromedriver")
browser.get("https://suninjuly.github.io/execute_script.html")
x = browser.find_element_by_id("input_value")
x = int(x.text)
y = calc(x)
#button = browser.find_element_by_tag_name("button")
button = browser.find_element_by_css_selector("[type='submit']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
button.click()
#browser.find_element_by_css_selector("[type='submit']").click()
