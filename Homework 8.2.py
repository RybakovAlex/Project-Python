# Урок 8. ООП. Полезные дополнения
"""
Пункт 2. Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на ноль. Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    pass


def get_divisible():
    return int(input("Введите делимое: "))


def get_divisor():
    value = int(input("Введите делитель: "))
    if value == 0:
        raise MyZeroDivisionError
    return value


while True:
    try:
        divisible = get_divisible()
        divisor = get_divisor()

        print(f"Результат = {divisible / divisor}")
    except MyZeroDivisionError:
        print("Ошибка! На ноль делить нельзя!")
    break
