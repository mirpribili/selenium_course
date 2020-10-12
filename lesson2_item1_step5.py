from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"



import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    #link = "http://suninjuly.github.io/simple_form_find_task.html"
    #browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера

    
    browser.get(link)
    time.sleep(1)


    #$x('//span[contains(text(),"What")]/text()')


    
    input3 = browser.find_element(By.XPATH, './/*[@id = "input_value"]')
    
    x = input3.text
    y = calc(int(x))


    input1 = browser.find_element(By.XPATH, './/*[@id = "answer"]')
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()



 
    #<button type="submit" class="btn" disabled="disabled">
    # Submit</button>
    
    # $x('.//button[text() = "Submit"]')

    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    #button = browser.find_element_by_css_selector("button.btn")
    button.click()




    #find_element_by_css_selector()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

    #browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла

