# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(*args):


    try:
        arg_1 = int(input("Введите первое число: "))
        arg_2 = int(input("Введите второе число: "))
        res = arg_1 // arg_2

    except ValueError:
        return "Неверное число"
    except ZeroDivisionError:
        return "Деление на ноль невозможно"

    return res

print(my_div())