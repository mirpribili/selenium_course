
############ lesson2_item4_step8.py

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



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
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
############ lesson3_item3_step3_test.py
from selenium import webdriver
import time
import os
import pytest

def setup_module(module):
    #init_something()
    pass

def teardown_module(module):
    #teardown_something()
    pass

def test_abs1():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element_by_xpath('.//label[text()=\'First name*\']/following-sibling::input').send_keys("pasha")
        browser.find_element_by_xpath('.//label[text()=\'Last name*\']/following-sibling::input').send_keys("zzzz")
        browser.find_element_by_xpath('.//label[text()=\'Email*\']/following-sibling::input').send_keys("pasha@ya.ru")
        browser.find_element_by_xpath(".//button[text()='Submit']").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Should be - Congratulations! You have successfully registered!"

def test_abs2():
    try: 
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first[required]")
        input1.send_keys("Vladimir")
        input2 = browser.find_element_by_css_selector(".second[required]")
        input2.send_keys("Lenin")
        input3 = browser.find_element_by_css_selector(".third[required]")
        input3.send_keys("USSR_1917@yandex.ru")

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
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Should be - Congratulations! You have successfully registered!"

if __name__ == "__main__":
	os.system ("pytest " + os.path.basename(__file__) + " --tb=line")

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
############ lesson3_item2_step13.py

'''

	Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
	Создайте новый файл
	Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
	Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
	Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
	Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
	Запустите получившиеся тесты из файла 
	Просмотрите отчёт о запуске и найдите последнюю строчку 
	Отправьте эту строчку в качестве ответа на это задание 



	Как и прежде загружаем модуль selenium и пользуемся им, как и в задаче - предке;
	
	Создаем класс в названии которого фигурирует "test_class_name";
	
	Наследуем (unittest.TestCase);
	
	Создаем две функции внутри класса, у меня они получились идентичными, за исключением содержимого переменной URL (ссылка на веб страницу);
	
	В функциях из предыдущего шага не используем конструкции try, except, finally и assert, используем только: self.assertEqual('что должно быть', 'что есть', 'что произошло');
	
	Добавляем в код: if __name__ == "__main__": unittest.main()
	
	Тест, очевидно, проваливается на втором линке, ищем одну короткую строку, которая нам об этом говорит. 

'''

from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):
	def test_abs1(self):
		try:
			browser = webdriver.Chrome()
			browser.maximize_window()
			browser.get("http://suninjuly.github.io/registration1.html")
			browser.find_element_by_xpath('.//label[text()=\'First name*\']/following-sibling::input').send_keys("pasha")
			browser.find_element_by_xpath('.//label[text()=\'Last name*\']/following-sibling::input').send_keys("zzzz")
			browser.find_element_by_xpath('.//label[text()=\'Email*\']/following-sibling::input').send_keys("pasha@ya.ru")
			browser.find_element_by_xpath(".//button[text()='Submit']").click()

			# Проверяем, что смогли зарегистрироваться
			# ждем загрузки страницы
			time.sleep(1)

			# находим элемент, содержащий текст
			welcome_text_elt = browser.find_element_by_tag_name("h1")
			# записываем в переменную welcome_text текст из элемента welcome_text_elt
			welcome_text = welcome_text_elt.text
		finally:
			# ожидание чтобы визуально оценить результаты прохождения скрипта
			time.sleep(3)
			# закрываем браузер после всех манипуляций
			browser.quit()
			# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be - Congratulations! You have successfully registered!")

	def test_abs2(self):
		try: 
			browser = webdriver.Chrome()
			link = "http://suninjuly.github.io/registration2.html"
			browser.get(link)
			# Ваш код, который заполняет обязательные поля
			input1 = browser.find_element_by_css_selector(".first[required]")
			input1.send_keys("Vladimir")
			input2 = browser.find_element_by_css_selector(".second[required]")
			input2.send_keys("Lenin")
			input3 = browser.find_element_by_css_selector(".third[required]")
			input3.send_keys("USSR_1917@yandex.ru")

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
		finally:
			# ожидание чтобы визуально оценить результаты прохождения скрипта
			time.sleep(3)
			# закрываем браузер после всех манипуляций
			browser.quit()
			# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be - Congratulations! You have successfully registered!")

if __name__ == "__main__":
	unittest.main()
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
############ methods.py
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
    pass
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson3_item2_step8.py

'''
	Дана функция test_input_text,  которая принимает два значения: expected_result — ожидаемый результат, и actual_result — фактический результат. Обратите внимание, input использовать не нужно!

	Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. 

	Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система! 

	Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" и протестируйте ваш код на разных введенных значениях, проверьте вывод вашей функции на разных парах. Обрабатывать ситуацию с пустым или невалидным вводом не нужно. 

	Sample Input 1:

	8 11

	Sample Output 1:

	expected 8, got 11

	Sample Input 2:

	11 11

	Sample Output 2:

	Sample Input 3:

	11 15

	Sample Output 3:

expected 11, got 15

'''
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result,\
    f"expected {expected_result}, got {actual_result}" 

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson2_item3_step6.py

'''
    Открыть страницу http://suninjuly.github.io/redirect_accept.html
    Нажать на кнопку
    Переключиться на новую вкладку
    Пройти капчу для робота и получить число-ответ
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/redirect_accept.html"

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


    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

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



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson2_item2_step8.py

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



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson3_item2_step9.py

'''
Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring. 

Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. 

Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система! 

Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" и протестируйте ваш код на разных введенных значениях, проверьте вывод вашей функции на разных парах. Обрабатывать ситуацию с пустым или невалидным вводом не нужно. 

Sample Input 1:

fulltext some_value

Sample Output 1:

expected 'some_value' to be substring of 'fulltext'

Sample Input 2:

1 1

Sample Output 2:

Sample Input 3:

some_text some

Sample Output 3:



'''

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
    



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson3_item4_step7_test.py
import os
import pytest

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":) \t very_important_fixture", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р \t print_smiling_faces", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        print("test_first_smiling_faces")

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        print("test_second_smiling_faces")


if __name__ == "__main__":
	os.system ("pytest " + os.path.basename(__file__) + " -s")
#  cd $HOME/selenium_course;python  ~/selenium_course/lesson3_item4_step7_test.py
'''
====================================== test session starts ======================================
platform linux -- Python 3.7.9, pytest-5.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/kde/selenium_course
collected 2 items                                                                               

lesson3_item4_step7_test.py ^_^ 

:-Р 

:) 

.:-Р 

.:3 



======================================= 2 passed in 0.02s =======================================
'''

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
############ lesson3_item5_step6_test_xfail.py
import pytest
import os

# Пометьте первый тест параметром, который в случае неожиданного прохождения теста,
# помеченного как xfail, отметит в отчете этот тест как упавший.


@pytest.mark.xfail(strict=True)  # strict=True
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

if __name__ == "__main__":
	os.system ("pytest " + os.path.basename(__file__) + " -s")
#cd $HOME/selenium_course;python  ~/selenium_course/lesson3_item5_step6_test_xfail.py
#conda deactivate; source $HOME/enviroments/selenium_env/bin/activate; cd $HOME/selenium_course;python  ~/selenium_course/lesson3_item5_step6_test_xfail.py

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson3_item5_step7.py
import pytest

@pytest.fixture
def browser():
    pass


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        print(1)
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        print(2)
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        print(3)
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        print(4)
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        print(5)
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        print(6)
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    print(7)
    assert True


#pytest -v -m "smoke and not beta_users" lesson3_item5_step7.py
#C первого раза. просто смотрите где есть smoke потом нет ли там "beta users", потому что не должно бить, потом смотрите будут ли тести skip или нет. если xfail есть то тест все равно будет исполняться.
# 1 4


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ lesson3_item6_step3.py
homework = '''
    Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: 

        открыть страницу 
        ввести правильный ответ 
        нажать кнопку "Отправить" 
        дождаться фидбека о том, что ответ правильный 
        проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

    Опциональный фидбек — это текст в черном поле, как показано на скриншоте: 


    Правильным ответом на задачу в заданных шагах является число:

    import time
    import math

    answer = math.log(int(time.time()))

    Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров: 

    https://stepik.org/lesson/236895/step/1
    https://stepik.org/lesson/236896/step/1
    https://stepik.org/lesson/236897/step/1
    https://stepik.org/lesson/236898/step/1
    https://stepik.org/lesson/236899/step/1
    https://stepik.org/lesson/236903/step/1
    https://stepik.org/lesson/236904/step/1
    https://stepik.org/lesson/236905/step/1

    Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно. 

    В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание. 

    Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают. 
'''

import math
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

correct_answer_text = "Correct!"

# Создаем кортеж со списком url
url_check = ("https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1")


@pytest.fixture(scope="function")  # Создаем фикустуру для запуска браузера
def browser():
    print("\n Start browser...")
    browser = webdriver.Chrome()
    yield browser
    print("\n Quit browser..")
    browser.quit()


@pytest.mark.parametrize('url', url_check)
def test_hidden_message(browser, url):
    link = f'{url}'
    browser.get(link)

    # Ждем появления текстового поля на странице в течении 10 сек
    # Находим поле ввода ответа на странице, и вставляем туда ответ math.log(int(time.time())
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.textarea"))
    )
    text_field = browser.find_element_by_css_selector("textarea.textarea")
    text_field.send_keys(str(math.log(int(time.time()))))  # Хорошо читается :/

    # Находим кнопку "Submit"
    # Нажимаем на нее
    submit_btn = browser.find_element_by_css_selector("button.submit-submission")
    submit_btn.click()

    # Ждем появления элемента "дополнительного фидбека" в течении 5 сек
    # Находим параметр text у найденого элемента
    # Сверяем text с искомым нами (correct_answer_text)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
    )
    find_answer_text = browser.find_element_by_css_selector("pre.smart-hints__hint")
    answer_text = find_answer_text.text

    try:
        assert answer_text == correct_answer_text, 'Text is not: "Correct!"'

    except Exception:
        raise AssertionError('Error! Text does not match')
    finally:
        print("----> " + answer_text + " <----")

# Смотриться лучше, но без assertError  не падает, браузер открыт всю сессию
# #from selenium import webdriver
# import pytest
# import time
# import math
#
# final = ''
#
#
# @pytest.fixture(scope="session")
# def browser():
#     br = webdriver.Chrome()
#     yield br
#     br.quit()
#     print(final)  # напечатать ответ про Сов в конце всей сессии
#
#
# @pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
# def test_find_hidden_text(browser, lesson):
#     global final
#     link = f'https://stepik.org/lesson/{lesson}/step/1'
#     browser.implicitly_wait(10)
#     browser.get(link)
#     answer = math.log(int(time.time()))
#     browser.find_element_by_css_selector('textarea').send_keys(str(answer))
#     browser.find_element_by_css_selector('.submit-submission ').click()
#     check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
#     try:
#         assert 'Correct!' == check_text
#     except AssertionError:
#         final += check_text  # собираем ответ про Сов с каждой ошибкой

#pytest -v  lesson3_item6_step3.py

answer = '''

E           AssertionError: Text is not: "Correct!"
E           assert 'The owls ' == 'Correct!'
E             - The owls 
E             + Correct!
E           AssertionError: Error! Text does not match
E           AssertionError: Text is not: "Correct!"
E           assert 'are not ' == 'Correct!'
E             - are not 
E             + Correct!
E           AssertionError: Error! Text does not match
E           AssertionError: Text is not: "Correct!"
E           assert 'what they seem! OvO' == 'Correct!'
E             - what they seem! OvO
E             + Correct!
E           AssertionError: Error! Text does not match


The owls are not what they seem! OvO
'''

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

#print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")





myCmd = 'sudo ls -la' 
os.system (myCmd)

#myCmd = "ping -c 1 8.8.8.8 &> /dev/null && echo success || echo fail & sudo service network-manager restart"
myCmd = "ping -c 1 8.8.8.8 &> /dev/null && echo success || sudo service network-manager restart"
myCmd = "ping -c 1 8.8.8.8 > txt.txt"
#myCmd = "ping -c 1 8.8.8.8"
i = 0
errors = 0
while True:
    time.sleep(2)
    i += 1
    #print(i)
    #print(f"{bcolors.WARNING}==={i}==={bcolors.ENDC}")
    print("i: "+ str(i))
    os.system(myCmd)
    f = open("txt.txt")
    read = f.read()
    #print(f.read())
    f.close()
    if not "time=" in read:
        os.system("sudo service network-manager restart")
        #https://stackoverflow.com/questions/48639609/sudo-pass-automatic-password-in-python
        #https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password
        #print(f"{bcolors.FAIL}Try reload{bcolors.ENDC}")
        print("reload")
        errors += 1
    else:
        #print(f"{bcolors.OKGREEN}OK. Continue... {errors}{bcolors.ENDC}")
        print("errors: " + str(errors))
    

	#myCmd = os.popen(myCmd).read()
	#print(myCmd)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
############ pytest_template_test.py
'''
https://coderlessons.com/tutorials/python-technologies/uznaite-pytest/pytest-kratkoe-rukovodstvo

import unittest

class TestUtilDate(unittest.TestCase):
    def setUp(self):
        #init_something()
        pass
        
    def tearDown(self):
        #teardown_something()
        pass
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        
    def test_failed_upper(self):
        self.assertEqual('foo'.upper(), 'FOo')
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilDate)
    unittest.TextTestRunner(verbosity=2).run(suite)

'''

# То же самое в PyTest:

import os
import pytest

def setup_module(module):
    #init_something()
    pass

def teardown_module(module):
    #teardown_something()
    pass

def test_upper():
    assert 'foo'.upper() == 'FOO'
    
def test_isupper():
    assert 'FOO'.isupper()
    
def test_failed_upper():
    assert 'foo'.upper() == 'FOo'

if __name__ == "__main__":
	os.system ("pytest " + os.path.basename(__file__) + " --tb=line ")
    #os.system ("pytest -v " + os.path.basename(__file__) + " --tb=line ")

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
############ lesson2_item3_step4.py

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
