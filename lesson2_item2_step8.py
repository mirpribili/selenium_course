
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


link = "http://suninjuly.github.io/file_input.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# <input type="text" name="firstname" class="form-control" 
# placeholder="Enter first name" required="" maxlength="32">

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.XPATH, './/*[@id = "input_value"]')
    
    input2 = browser.find_element(By.XPATH, './/*[@id = "answer"]')
    input2.send_keys(
    	calc(input1.text)
    	)

    browser.execute_script("window.scrollBy(0, 100);")

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    option2 = browser.find_element(By.XPATH, './/*[@id = "robotsRule"]')
    option2.click()


    #browser.execute_script("alert('Robots at work " + input1.text + "');")
    #time.sleep(2)

    browser.execute_script('''button = document.getElementsByTagName("button")[0];
	button.scrollIntoView(true);''')
    time.sleep(1)

    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

    #browser.close()
    time.sleep(2)
    browser.quit()


