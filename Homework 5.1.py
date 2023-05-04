# Урок 5. Работа с файлами
"""
Пункт 1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

my_file = open('file_5_1.txt', 'w')
line = input('Введите текст: \n')
while line:
    my_file.writelines(line)
    line = input('Нажмите "Enter" для завершения ввода текста!\n')
    if not line:
        break
my_file.close()
my_file = open('file_5_1.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
