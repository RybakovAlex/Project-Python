# Урок 5. Работа с файлами
"""
Пункт 2. Создать текстовый файл (не программно), сохранить в нём
несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

my_file = open('file_5_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n{content}')
my_file = open('file_5_2.txt', 'r')
content = my_file.readlines()
print(f'Кол-во строк в файле - {len(content)}')
my_file = open('file_5_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Кол-во символов {i + 1}-ой строки - {len(content[i])}')
my_file = open('file_5_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Кол-во слов - {len(content)}')
my_file.close()
