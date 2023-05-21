# Урок 8. ООП. Полезные дополнения
"""
   Пункт 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым для
классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
ксерокс). В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа
оргтехники.
   Пункт 5. Продолжить работу над первым заданием. Разработайте методы,
которые отвечают за приём оргтехники на склад и передачу в определённое
подразделение компании. Для хранения данных о наименовании и количестве
единиц оргтехники, а также других данных, можно использовать любую подходящую
структуру (например, словарь).
   Пункт 6. Продолжить работу над вторым заданием. Реализуйте механизм
валидации вводимых пользователем данных. Например, для указания количества
принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум
возможностей, изученных на уроках по ООП.
"""


class Warehouse():

    def __init__(self, warehouse_id, warehouse_name, warehouse_address,
                 **warehouse_dev):
        self.warehouse_id = warehouse_id
        self.warehouse_name = warehouse_name
        self.warehouse_address = warehouse_address
        self.warehouse_dev = warehouse_dev

    def warehouse_info(self):
        print(f'\nid-склада: {self.warehouse_id}'
              f'\nНазвание склада: {self.warehouse_name}'
              f'\nАдрес склада: {self.warehouse_address}')

    def check_count(self, dev_count):
        """ проверка остатков на складе"""
        ret_val = True
        for dev, count in dev_count.items():
            if dev not in self.warehouse_dev:
                print(
                    f'\nНа складе {self.warehouse_name}\n'
                    f' товар с id {dev.id} {dev.model_name} отсутствует!')
                ret_val = False
                break
            elif self.warehouse_dev[dev] < count:
                print(
                    f'\nНа складе {self.warehouse_name} \n'
                    f' товар с id {dev.id} {dev.model_name}\
                    отсутствует в нужном количестве!')
                ret_val = False
                break
        return ret_val

    def move_dev(self, move_type, dev_count):
        if move_type == 'in':  # перемещение на склад
            print(f'\nПеремещение на склад {self.warehouse_name}:')
            for dev, count in dev_count.items():
                print(f' товар с id {dev.id} - {dev.model_name}: {count} шт')
                if dev not in self.warehouse_dev:
                    self.warehouse_dev[dev] = count
                else:
                    self.warehouse_dev[dev] += count
        elif move_type == 'out':  # перемещение со склада
            print(f'\nПеремещение со склада {self.warehouse_name}:')
            for dev, count in dev_count.items():
                print(f' товар с id {dev.id} - {dev.model_name}: {count} шт.')
                self.warehouse_dev[dev] -= count

    def print_dev_count(self):
        print(f'На складе {self.warehouse_name}')
        for key, value in self.warehouse_dev.items():
            print(f' товар с id {key.id} - {key.model_name} {value} шт.')


class Devices():
    def __init__(self, id, model_name, serial_num, country):
        self.id = id
        self.model_name = model_name
        self.serial_num = serial_num
        self.country = country

    def info(self):
        print(f'id: {self.id}'
              f'\nНаименование модели: {self.model_name}'
              f'\nСерийный номер: {self.serial_num}'
              f'\nСтрана-производитель: {self.country}')
        super().info()


class Printer(Devices):
    def __init__(self, id, model_name, serial_num, country, printer_type, led):
        self.type = 'Принтер'
        self.printer_type = printer_type
        self.led = led
        super().__init__(id, model_name, serial_num, country)

    def info(self):
        print(f'\nТип устройства: {self.type}'
              f'\nТип принтера: {self.printer_type}'
              f'\nLED-технология: {self.led}')
        super().info()


class Scanner(Devices):
    def __init__(self, id, model_name, serial_num, country, scanner_type, spd,
                 dpi):
        self.type = 'Сканер'
        self.scanner_type = scanner_type
        self.spd = spd
        self.dpi = dpi
        super().__init__(id, model_name, serial_num, country)

    def info(self):
        print(f'\nТип устройства: {self.type}'
              f'\nТип сканера: {self.scanner_type}'
              f'\nСкорость: {self.spd}'
              f'\nРазрешение: {self.dpi}')
        super().info()


class Copier(Devices):
    def __init__(self, id, model_name, serial_num, country, copier_type, color,
                 lumen):
        self.type = 'Копир'
        self.copier_type = copier_type
        self.color = color
        self.lumen = lumen
        super().__init__(id, model_name, serial_num, country)

    def info(self):
        print(f'\nТип устройства: {self.type}'
              f'\nТип копира: {self.copier_type}'
              f'\nЦвет: {self.color}'
              f'\nСветовой поток: {self.lumen}')
        super().info()


warehouse_lst = []
dev_lst = []

warehouse_lst.append(Warehouse(1, 'Москва', 'Москва, ул. Пушкина, д. 1'))
warehouse_lst.append(Warehouse(2, 'МО', 'МО, г.Химки, ул. 9-го Мая, д. 2'))
warehouse_lst.append(Warehouse(3, 'СПБ', 'СПБ, Невский проспект, д. 3'))

print(f'\n*** Склады ***')
warehouse_lst[0].warehouse_info()
warehouse_lst[1].warehouse_info()
warehouse_lst[2].warehouse_info()

dev_lst.append(
    Copier(1, 'Xerox workcentre', '1234', 'China', 'МФУ', 'Цветной', '3000'))
dev_lst.append(
    Printer(2, 'HP LaserJet', '5678', 'China', 'laser', 'Led'))
dev_lst.append(
    Scanner(3, 'Epson Eco', '1213', 'Japan', 'МФУ', '15 стр/мин', '600 dpi'))
dev_lst.append(
    Scanner(4, 'Epson Force', '910', 'China', 'МФУ', '17 стр/мин', '900 dpi'))

print(f'\n* Поступление товара на склад *')
warehouse_lst[0].move_dev('in', {dev_lst[0]: 2, dev_lst[1]: 4, dev_lst[2]: 6})
warehouse_lst[1].move_dev('in', {dev_lst[0]: 2, dev_lst[1]: 3, dev_lst[2]: 4})
warehouse_lst[2].move_dev('in', {dev_lst[2]: 1, dev_lst[3]: 2, dev_lst[1]: 3})


def check_warehouse(warehouse_id):
    # проверка пользовательского ввода номера склада
    warehouse = None
    for i in warehouse_lst:
        if i.warehouse_id == warehouse_id:
            warehouse = i
            break

    return warehouse


def print_warehouse_list():
    for i, warehouse in enumerate(warehouse_lst):
        print(f'{i + 1}. {warehouse.warehouse_name}')


def get_warehouse(msg):
    print(msg)
    print_warehouse_list()
    warehouse_id = input(
        'Введите id склада или нажмите Enter отмены действия: ')

    warehouse = None
    try:
        warehouse_id = int(warehouse_id)
    except ValueError:
        print('Некорректный ввод числа (id-склада) или строка пустая!')
    else:
        warehouse = check_warehouse(warehouse_id)
        if not warehouse:
            print('Склад с указанным id-склада не существует!')

    return warehouse


def get_dev_by_id(dev_id):
    dev = None
    for i in dev_lst:
        if i.id == dev_id:
            dev = i
            break

    return dev


def parse_dev_count(warehouse, str_dev_count):
    dev_count = {}
    warehouse = None

    try:
        lst1 = str_dev_count.split(',')
    except:
        print(f'Ошибка при обработке введенной строки: {str_dev_count}')
    else:
        for i in lst1:
            try:
                parse_dev_id, parse_dev_count = i.split(' ')
                parse_dev_id = int(parse_dev_id)
                parse_dev_count = int(parse_dev_count)
            except:
                print(
                    f'Ошибка ввода данных: {i}, повторите ввод!')
            else:
                dev = get_dev_by_id(parse_dev_id)
                if not dev:
                    print(
                        f'Товар с id {parse_dev_id} не найден в справочнике!')
                else:
                    dev_count[dev] = parse_dev_count

    return dev_count


while True:
    from_warehouse = None
    to_warehouse = None
    dev_count = None

    from_warehouse = get_warehouse(
        '\nДля перемещения товара выберите склад-источник: ')
    if not from_warehouse:
        print('Действие отменено!')
        break

    to_warehouse = get_warehouse('\nВыберите склад-получатель: ')
    if not to_warehouse:
        print('Действие отменено!')
        break

    from_warehouse.print_dev_count()
    str_dev_count = input(
        'Введите через пробел id товара и необходимое кол-во: ')

    dev_count = parse_dev_count(from_warehouse, str_dev_count)
    if len(dev_count) == 0:
        print('Не удалось распознать введенную строку!')
    else:
        if from_warehouse.check_count(dev_count):
            from_warehouse.move_dev('out', dev_count)
            to_warehouse.move_dev('in', dev_count)
            print(
                '\nПеремещение товара выполнено успешно!\n'
                'Остатки товара на складах после перемещения:')
            from_warehouse.print_dev_count()
            to_warehouse.print_dev_count()
        else:
            print('Перемещение товаров не выполнено!')
