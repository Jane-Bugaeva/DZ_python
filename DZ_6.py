'''
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

a1 = int(input('Введите первый элемент массива: '))
d = int(input('Введите шаг: '))
n = int(input('Введите количество элементов: '))
list_massiv = []
for i in range(n):
    an = (a1 + i * d)
    list_massiv.append(an)
print(list_massiv)

'''
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
'''

size = int(input('Input size '))
list_1 = [random.randint(0, 10) for _ in range(size)]
print(list_1)
list_2 = []
min = int(input('input min quantity '))
max = int(input('inpit max quantity '))
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        list_2.append(i)
print(list_2)
