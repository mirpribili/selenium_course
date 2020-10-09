
############ lesson1_item6_step11.py

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    #elements = browser.find_elements_by_tag_name("input")
    elements = browser.find_elements_by_css_selector('input[required]')
    for element in elements:
        element.send_keys("Мой ответ")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson1_item6_step8.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

value1 ="input"
value2 ="last_name"
value3 ="city"
value4 ="country"



try:
    browser = webdriver.Chrome()
    #link = "http://suninjuly.github.io/simple_form_find_task.html"
    #browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера

    
    browser.get(link)
    time.sleep(1)


    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")


 
    #<button type="submit" class="btn" disabled="disabled">
    # Submit</button>
    
    # $x('.//button[text() = "Submit"]')

    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    #button = browser.find_element_by_css_selector("button.btn")
    button.click()




    #find_element_by_css_selector()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций

    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ 1_4.py
# 1.4
"""
$x('.//button[text() = "Gold"]')
"""

#1.5
"""
.card-body:nth-child(1) p
{
    color:blue;
}

p.text
{
    color:blue;
}

.watermelon p.description
{
    color:blue;
}

.banana p
{
    color:blue;
}
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson1_item6_step11b.py
from selenium import webdriver
try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/registration1.html")
    browser.find_element_by_xpath('.//label[text()=\'First name*\']/following-sibling::input').send_keys("pasha")
    browser.find_element_by_xpath('.//label[text()=\'Last name*\']/following-sibling::input').send_keys("zzzz")
    browser.find_element_by_xpath('.//label[text()=\'Email*\']/following-sibling::input').send_keys("pasha@ya.ru")
    browser.find_element_by_xpath(".//button[text()='Submit']").click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson1_item6_step5.py
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

value1 ="input"
value2 ="last_name"
value3 ="city"
value4 ="country"


try:
    browser = webdriver.Chrome()
    #link = "http://suninjuly.github.io/simple_form_find_task.html"
    #browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера

    browser.get(link)


    # Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код: 
    link = browser.find_element_by_link_text(str(str(math.ceil(math.pow(math.pi, math.e)*10000))))
    link.click()

    # А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код: 

    # link = browser.find_element_by_partial_link_text("examples")
    # link.click()

    time.sleep(1)


    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #find_element_by_css_selector()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций

    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson1_item6_step10.py

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    #elements = browser.find_elements_by_tag_name("input")
    elements = browser.find_elements_by_css_selector('input[required]')
    for element in elements:
        element.send_keys("Мой ответ")
        

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson1_item6_step7.py

from selenium import webdriver

import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    time.sleep(5)

    # alert = browser.switch_to_alert()
    # print (alert.text) 

    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson1_item6_step4.py
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

value1 ="input"
value2 ="last_name"
value3 ="city"
value4 ="country"


try:
    browser = webdriver.Chrome()
    #link = "http://suninjuly.github.io/simple_form_find_task.html"
    #browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера

    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    #find_element_by_css_selector()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций

    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson2_item1_step5.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

value1 ="input"
value2 ="last_name"
value3 ="city"
value4 ="country"



try:
    browser = webdriver.Chrome()
    #link = "http://suninjuly.github.io/simple_form_find_task.html"
    #browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера

    
    browser.get(link)
    time.sleep(1)


    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")


 
    #<button type="submit" class="btn" disabled="disabled">
    # Submit</button>
    
    # $x('.//button[text() = "Submit"]')

    button = browser.find_element(By.XPATH, './/button[text() = "Submit"]')
    #button = browser.find_element_by_css_selector("button.btn")
    button.click()




    #find_element_by_css_selector()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций

    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ get_method.py
import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(15)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(15)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(15)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(15)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson1_item6_step11c.py
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input")
    name.send_keys("Ivan")
    sname = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input")
    sname.send_keys("Petrov")
    email = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")
    email.send_keys("sss@sss.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
