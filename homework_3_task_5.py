import sys

result = 0
while True:
    line = input("Введите число либо Q для выхода: ")
    symbols = line.split(" ")
    for symbol in symbols:
        try:
            number = float(symbol)
            result += number
        except:
            if symbol == 'q' or 'Q':
                print(f"Результат расчёта {result}. Программа прервана")
            else:
                print(f"Сумма данных расчётов {result}. Input error", file=sys.stderr)