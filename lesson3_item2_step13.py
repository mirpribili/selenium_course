
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

'''

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
    


