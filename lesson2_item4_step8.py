
'''
    
    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import methods
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"


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


    WebDriverWait(browser, 12).until(
        #EC.text_to_be_present_in_element((By.ID, "тут id"), "тут цена"))
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
 

    button = browser.find_element(By.XPATH, './/button[text() = "Book"]')
    button.click()

    time.sleep(1)


    input3 = browser.find_element(By.XPATH, './/*[@id = "input_value"]')
    x = input3.text
    y = methods.calc(int(x))


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


