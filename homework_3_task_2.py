# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input("Введите имя: ")
lastname = input("Введите фимилию: ")
year = int(input("Введите год рождения: "))
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone = input("Введите телефон: ")


def my_func(name, lastname, year, city, email, phone):
    return ' '.join([name, lastname, year, city, email, phone])


print(my_func('name', 'lastname', 'year', 'city', 'email', 'phone'))
# никак не могу понять как вывести значения введенные пользователем, выводятся только названия переменных


