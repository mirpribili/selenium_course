
'''
    Открыть страницу http://suninjuly.github.io/alert_accept.html
    Нажать на кнопку
    Принять confirm
    На новой странице решить капчу для роботов, чтобы получить число с ответом
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# <input type="text" name="firstname" class="form-control" 
# placeholder="Enter first name" required="" maxlength="32">

# $("[name*='email']")
# $x('.//button[text() = "Submit"]')
# //input[@id='firstName']
# //input[@type='text'] 
# 1)Driver.FindElement(By.XPath("//input[@id='firstName']"));
# 2)Driver.FindElement(By.Id("firstName"));
# 3)Driver.FindElement(By.CssSelector("#firstName"));
# //*[text()[contains(.,'firstName')]]
## $x(".//input[@name='email']")


try:
    browser = webdriver.Chrome()
    browser.get(link)
 

    button = browser.find_element(By.XPATH, './/button[text()]')
    button.click()


    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)


    input3 = browser.find_element(By.XPATH, './/*[@id = "input_value"]')
    x = input3.text
    y = calc(int(x))


    input1 = browser.find_element(By.XPATH, './/*[@id = "answer"]')
    input1.send_keys(y)


    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

    #browser.close()
    time.sleep(2)
    browser.quit()


