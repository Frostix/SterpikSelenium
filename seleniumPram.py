import pytest
from selenium import webdriver
import time
import math


answer = math.log(int(time.time()))
steps =  ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("e:\\Chromedriver\\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('step', steps)
def test_guest_should_see_login_link(browser, step):
    link = "https://stepik.org/lesson/{}/step/1".format(step)
    browser.get(link)
    browser.implicitly_wait(10)
    text = browser.find_element_by_class_name("textarea")
    
    answer = math.log(int(time.time()))
    text.send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    assert browser.find_element_by_class_name("smart-hints__hint").text == "Correct!"

    

    

