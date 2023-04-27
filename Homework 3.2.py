# Урок 3. Функции
"""
Пункт 2. Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def personal_data(first_name, last_name, year_of_birth, city, email, phone):
    return print(
        f'Имя: {first_name} Фамилия: {last_name} Год рождения: {year_of_birth}' 
        f' Город проживания: {city} Email: {email} Телефон: {phone}')


personal_data(
    first_name=input('Введите имя: '),
    last_name=input('Введите фамилию: '),
    year_of_birth=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    email=input('Введите email: '),
    phone=input('Введите телефон: '),
)
