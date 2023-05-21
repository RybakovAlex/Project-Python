# Урок 7. ООП. Продвинутый уровень
"""
Пункт 2. Реализовать проект расчёта суммарного расхода ткани
на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, size_v, height_h):
        self.size_v = size_v
        self.height_h = height_h

    def get_area_c(self):
        return self.size_v / 6.5 + 0.5

    def get_area_s(self):
        return self.height_h * 2 + 0.3

    @property
    def get_area_full(self):
        return str(f'Общий расход ткани: \n'
                   f'{(self.size_v / 6.5 + 0.5) + (self.height_h * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, size_v, height_h):
        super().__init__(size_v, height_h)
        self.area_c = round(self.size_v / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.area_c}'


class Suit(Clothes):
    def __init__(self, size_v, height_h):
        super().__init__(size_v, height_h)
        self.area_s = round(self.height_h * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.area_s}'


coat = Coat(8, 5)
suit = Suit(8, 5)
print(coat)
print(suit)
print(coat.get_area_full)
