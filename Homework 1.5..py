# Урок 1. Знакомство с Python
"""
Пункт 5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки. Выведите соответствующее сообщение.
"""

revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
profit = 0       # revenue > costs = прибыль (выручка > издержек)

if revenue > costs:
    print("Финансовый результат работы фирмы - прибыль")
else:
    print("Финансовый результат работы фирмы - убыток")
