
# Шпаргалка по xpath и css селекторам
# https://devhints.io/xpath\


'''
    Открыть страницу http://suninjuly.github.io/get_attribute.html.
    Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    Посчитать математическую функцию от x (сама функция остаётся неизменной).
    Ввести ответ в текстовое поле.
    Отметить checkbox "I'm the robot".
    Выбрать radiobutton "Robots rule!".
    Нажать на кнопку "Submit".
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, './/*[@id = "treasure"]')
    answer = input1.get_attribute("valuex")
    input2 = browser.find_element(By.XPATH, './/*[@id = "answer"]')
    input2.send_keys(
    	calc(answer)
    	)


    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.XPATH, './/*[@id = "robotsRule"]')
    option2.click()

    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    button.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

    #browser.close()
    time.sleep(2)
    browser.quit()


