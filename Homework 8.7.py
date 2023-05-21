# Урок 8. ООП. Полезные дополнения
"""
Пункт 7.  Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения
и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте
экземпляры класса (комплексные числа), выполните сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + bj'

    def __add__(self, other):
        print(f'Сложение комплексных чисел')
        return f'z = {self.a + other.a} + {self.b + other.b}j'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел')
        return f'z = {self.a * other.a - (self.b * other.b)} +\
{self.b * other.b}j'

    def __str__(self):
        return f'z = {self.a} + {self.b}j'


z_1 = ComplexNumber(1, 2)
z_2 = ComplexNumber(2, 4)
print(f'Комплексное число 1: {z_1}')
print(f'Комплексное число 2: {z_2}')
print(z_1 + z_2)
print(z_1 * z_2)
