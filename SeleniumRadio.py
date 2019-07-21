from selenium import webdriver
from math import ln, abs, sin

def calc(x):
  return str(ln(abs(12*sin(x))))


browser = webdriver.Chrome("C:\Chromedriver\chromedriver")
browser.get("https://suninjuly.github.io/execute_script.html")
x = browser.find_element_by_id("input_value")
x = int(x.get_text())
y = calc(x)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
button.click()
#browser.find_element_by_css_selector("[type='submit']").click()
