# Урок 5. Работа с файлами
"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле
выводить её на экран.
"""


def summary():
    try:
        with open('file_5_5.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except ValueError:
        print('Ошибка! Некорректный ввод!')


summary()
