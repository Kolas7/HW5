# В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы. [02-7.2-HL08]

text = input("Введите строку:")

for i in text.split(" "):
    print(i[::-1], end=" ")