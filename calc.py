
a = (input("Введите первый аргумент: "))
b = (input("Введите второй аргумент: "))
symbol = input("Выберите действие аргументов\n"
               "('+' - Сложение, '-' - Вычитание, \n"
               "'*' - Умножение, '**' - Возведение в степень, \n"
               "'/' - Деление, '//' - Целочисленное деление, \n"
               "'%' - Остаток от деления)\n")


def func(a, b, symbol):
    try:
        if symbol == "+":
            return int(a) + int(b)
        elif symbol == "-":
            return int(a) - int(b)
        elif symbol == "*":
            return int(a) * int(b)
        elif symbol == "**":
            return int(a) ** int(b)
        elif symbol == "/":
            return int(a) / int(b)
        elif symbol == "//":
            return int(a) // int(b)
        elif symbol == "%":
            return int(a) % int(b)
    except:
        return 0


a = func(a, b, symbol)

while True:
    print(a)
    if a != 0:
        b = (input("Введите второй аргумент: "))
        symbol = input("Выберите действие аргументов\n"
                       "('+' - Сложение, '-' - Вычитание, \n"
                       "'*' - Умножение, '**' - Возведение в степень, \n"
                       "'/' - Деление, '//' - Целочисленное деление, \n"
                       "'%' - Остаток от деления)\n")
    else:
        a = (input("Введите первый аргумент: "))
        b = (input("Введите второй аргумент: "))
        symbol = input("Выберите действие аргументов\n"
                       "('+' - Сложение, '-' - Вычитание, \n"
                       "'*' - Умножение, '**' - Возведение в степень, \n"
                       "'/' - Деление, '//' - Целочисленное деление, \n"
                       "'%' - Остаток от деления)\n")
    a = func(a, b, symbol)


