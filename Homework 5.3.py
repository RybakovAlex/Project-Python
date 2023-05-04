# Урок 5. Работа с файлами
"""
Пункт 3. Создать текстовый файл (не программно). Построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def workers_statistics():
    workers = [['Сидоров ', '12000 \n'], ['Кукушкин ', '19000 \n'],
               ['Иванов ', '145000 \n'], ['Смирнов ', '80000']]
    try:
        with open('file_5_3.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(
            f'Средняя величина дохода сотрудников равна \n'
            f'{sum / len(workers) / 12:.2f}')
            print(
            f'Меньше 20 тыс. получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'
