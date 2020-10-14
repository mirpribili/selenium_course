
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