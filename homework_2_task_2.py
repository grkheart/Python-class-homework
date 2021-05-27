# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


#exchange_List = int(input("Enter any 10 characters to exchange list: "))
exchange_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # так и не понял как реализовать ввод списка через input()
if len(exchange_List) % 2 == 0:
    i = 0
    while i < len(exchange_List):
        n = exchange_List[i]
        exchange_List[i] = exchange_List[i + 1]
        exchange_List[i + 1] = n
        i += 2
else:
    i = 0
    while i < len(exchange_List) - 1:
       n = exchange_List[i]
       exchange_List[i] = exchange_List[i + 1]
       exchange_List[i + 1] = n
       i += 2
print(exchange_List)