# Урок 6. Объектно-ориентированное программирование
"""
Пункт 4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed,color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    # атрибуты класса
    name = ()
    color = ()
    is_police = ()
    speed = ()

    # методы класса
    def go(self):
        print(f'{self.name} начал движение')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')


class TownCar(Car):

    def __init__(self, name, color):
        self.name = 'Lada Granta'
        self.color = 'черный'
        self.is_police = False
        self.speed_limit = 60
        print(f'1-й автомобиль {name}, цвет {color}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed > self.speed_limit:
            print('Внимание! Превышение допустимой скорости!')


class SportCar(Car):

    def __init__(self, name, color):
        self.name = 'LADA Vesta Sport'
        self.color = 'красный'
        self.is_police = False
        self.speed_limit = (120)
        print(f'2-й автомобиль {name}, цвет {color}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed > self.speed_limit:
            print('Внимание! Превышение допустимой скорости!')


class WorkCar(Car):

    def __init__(self, name, color):
        self.name = 'ГАЗель 3302'
        self.color = 'белый'
        self.is_police = False
        self.speed_limit = 40
        print(f'3-й автомобиль {name}, цвет {color}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed > self.speed_limit:
            print('Внимание! Превышение допустимой скорости!')


class PoliceCar(Car):

    def __init__(self, name, color):
        self.name = 'ВАЗ 2115'
        self.color = 'белый'
        self.is_police = True
        self.speed_limit = 60
        print(f'4-й автомобиль {name}, цвет {color}')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed > self.speed_limit and not self.is_police:
            print('Внимание! Превышение допустимой скорости!')


my_TownCar = TownCar('Lada Granta', 'черный')
my_TownCar.go()
my_TownCar.show_speed(50)
my_TownCar.show_speed(60)
my_TownCar.show_speed(70)
my_TownCar.turn('направо')
my_TownCar.turn('налево')
my_TownCar.stop()
print()

my_SportCar = SportCar('LADA Vesta Sport', 'красный')
my_SportCar.go()
my_SportCar.show_speed(60)
my_SportCar.show_speed(70)
my_SportCar.show_speed(80)
my_SportCar.turn('налево')
my_SportCar.turn('направо')
my_SportCar.stop()
print()

my_WorkCar = WorkCar('ГАЗель 3302', 'белый')
my_WorkCar.go()
my_WorkCar.show_speed(20)
my_WorkCar.show_speed(40)
my_WorkCar.show_speed(60)
my_WorkCar.stop()
print()

my_PoliceCar = PoliceCar('ВАЗ 2115', 'белый')
my_PoliceCar.go()
my_PoliceCar.show_speed(40)
my_PoliceCar.show_speed(60)
my_PoliceCar.show_speed(70)
my_PoliceCar.stop()
print()
