
'''

    
    
    Открыть страницу http://suninjuly.github.io/file_input.html
    Заполнить текстовые поля: имя, фамилия, email
    Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    Нажать кнопку "Submit"



'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/file_input.html"

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


    input1 = browser.find_element(By.XPATH, './/*[@name = "firstname"]')
    input1.send_keys("firstname")
    
    input2 = browser.find_element(By.XPATH, './/*[@name = "lastname"]')
    input2.send_keys("lastname")

    input3 = browser.find_element(By.XPATH, './/*[@name = "email"]')
    input3.send_keys("email")


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'txt.txt')
    
    element = browser.find_element(By.XPATH, './/*[@name = "file"]')
    element.send_keys(file_path)


    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

    #browser.close()
    time.sleep(2)
    browser.quit()


