
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
############ lesson2_item2_step6.py

'''

    
    Открыть страницу http://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскроллить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".


'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


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



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson2_item1_step7.py

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
############ for quick search in all files.py
"""
https://coursehunter.net/course/python-razrabotchik
https://coursehunter.net/course/full-stack-delaem-klon-airbnb-s-python-django-tailwind
DOPOLNITELNO https://coursehunter.net/course/python-django-dev-to-deployment
https://coursehunter.net/course/izuchite-python-i-eticheskiy-vzlom-s-nulya
https://coursehunter.net/course/fullstack-flask-sozdayte-prilozhenie-saas-s-pomoshchyu-flask
https://coursehunter.net/course/rest-apis-s-flask-i-python
"""

import os
from os.path import abspath

name_file = os.path.basename(__file__)
len_name = len(name_file)

directory = abspath(__file__)
directory = directory[0:-len_name]

print("*"+directory)

files = os.listdir(directory)
print("files:", files)

py = filter(lambda x: x.endswith('.py'), files)
print(" -"*25)


name_file_result = name_file[0:-3]+'_RESULT.py'
all_texts = ""

for p in py:
	if p != name_file_result:
		print(p)

		f = open(p)
		#print(f.read())
		all_texts += "\n############ " + p + "\n"
		all_texts += f.read()
		all_texts += "\n#" + "- "*100

		f.close()

#print(all_texts)

f = open(name_file_result, 'w')
f.write(all_texts + '\n')
f.close()

print("OK")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson2_item2_step8.py

'''

    
    Открыть страницу http://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскроллить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".


'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


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



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson2_item1_step6.py
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

#проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

#проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

#проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

finally:
    # закрываем браузер после всех манипуляций
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
############ os_mint.py

#cd $HOME/selenium_course; python os_mint.py
# https://andreyex.ru/yazyk-programmirovaniya-python/vypolnenie-komand-obolochki-s-python/

import os
import time 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

myCmd = 'ls -la' 
os.system (myCmd)

#myCmd = "ping -c 1 8.8.8.8 &> /dev/null && echo success || echo fail & sudo service network-manager restart"
myCmd = "ping -c 1 8.8.8.8 &> /dev/null && echo success || sudo service network-manager restart"

#myCmd = "ping -c 1 8.8.8.8"
i = 0
while True:
	time.sleep(2)
	i += 1
	#print(i)
	print(f"{bcolors.WARNING}==={i}==={bcolors.ENDC}")
	os.system(myCmd)

	#myCmd = os.popen(myCmd).read()
	#print(myCmd)


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
############ lesson2_item2_step3.py

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



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
