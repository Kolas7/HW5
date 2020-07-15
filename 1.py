while True:
    sing = input(f'выберите операцию (+,-,/,*) для выхода напишите 0\n:')
    if sing == '0':
        break
    x = int(input('первое число :'))
    y = int(input('второе число :'))
    if sing == '+':
        z = x + y
        print(z)
    elif sing == '-':
        z = x - y
        print(z)
    elif sing == '/':
        z = (x / y) if y != 0 else 0
        print(z)
    elif sing == '*':
        z = x * y
        print(z)
    else:
        print('некоректный ввод :')