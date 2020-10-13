
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
    


