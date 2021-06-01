# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

word = input("Введите слово в строчном формате: ")

def int_func(word):
    return word.title()
print (int_func(word))


