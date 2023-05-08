# Урок 6. Объектно-ориентированное программирование
"""
Пункт 1. Создать класс TrafficLight (светофор). Определить у него один атрибут
color (цвет) и метод running (запуск); атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы:
красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    # Время ожидания
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 5

    # Названия цветов
    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.waiting = None
        self.__color = color
        print(
            f'\nСоздан светофор TrafficLight')

    def start_light(self, color, waiting):
        self.waiting = waiting
        print(f'Включен {color} свет, подождите {self.waiting} сек')
        time.sleep(self.waiting)

    def running(self, color=''):

        # Если цвет не указан, вызов из родительского класса
        # Иначе если, старт со цвета, указанного при вызове метода
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.start_light('красный', self.red_color_wait)
            self.start_light('желтый', self.yellow_color_wait)
            self.start_light('зеленый', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.start_light('желтый', self.yellow_color_wait)
            self.start_light('зеленый', self.green_color_wait)
        else:
            self.start_light('зеленый', self.green_color_wait)

        print('Переключение цветов светофора завершено')


tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()
