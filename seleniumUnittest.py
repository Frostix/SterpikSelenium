from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
assertion =  "Поздравляем! Вы успешно зарегистировались!"


def registration(link):
    browser = webdriver.Chrome("C:\Chromedriver\chromedriver")
    browser.get(link)
    reuqired_fields = ["Имя*", "Фамилия*", "Email*"]

    for field in reuqired_fields:
        browser.find_element_by_xpath(f"//label[text()='{field}']/following-sibling::input").send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    return welcome_text

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(registration(link1), assertion, "Registration failed")
        
    def test_abs2(self):
        self.assertEqual(registration(link2), assertion, "Registration failed")
        
if __name__ == "__main__":
    unittest.main()


#assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text