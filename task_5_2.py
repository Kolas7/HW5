# Дано число. Найти сумму и произведение его цифр.
n = int(input('введите число :'))
s = 0
m = 1
while n>0:
    s += n%10
    m *= n%10
    n = n//10
print('Суммa:', s)
print('Произведение:', m)