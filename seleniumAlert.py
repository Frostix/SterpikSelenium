from selenium import webdriver
from math import sin, log

def calc(x):
  return str(log(abs(12*sin(x))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome("C:\Chromedriver\chromedriver")
browser.get(link)


button = browser.find_element_by_class_name("btn-primary")
button.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element_by_id("input_value")
x = int(x.text)
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)

button = browser.find_element_by_class_name("btn-primary")
button.click()

"""
input1 = browser.find_element_by_name("firstname")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("@")
input4 = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
input4.send_keys(file_path)
button = browser.find_element_by_class_name("btn-primary")
button.click()
"""