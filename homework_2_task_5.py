# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных
# чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

num = int(input("Введите число: "))
my_list = [7, 5, 3, 3, 2]
a = my_list.count(num)
for digit in my_list:
    if a > 0:
        i = my_list.index(num)
        my_list.insert(i + a, num)
        break
    else:
        if num > digit:
            b = my_list.index(digit)
            my_list.insert(b, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)
