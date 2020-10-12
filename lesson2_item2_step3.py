
'''

    Открыть страницу http://suninjuly.github.io/selects1.html
    Посчитать сумму заданных чисел
    Выбрать в выпадающем списке значение равное расчитанной сумме
    Нажать кнопку "Submit"

'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, './/*[@id = "num1"]')
    input2 = browser.find_element(By.XPATH, './/*[@id = "num2"]')
    print(input1.text)
    result = str( int(input1.text) + int(input2.text) )
    print(result)


    input3 = browser.find_element(By.XPATH, './/*[@id = "dropdown"]')
    select = Select( input3 )
    select.select_by_value(result)
    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

    #browser.close()
    time.sleep(2)
    browser.quit()


