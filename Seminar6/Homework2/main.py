# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random

def int_input(word):
        try:
            temp = int(input(word))
            return temp
        except:
            print("Вы ошиблись, попробуйте еще раз")
            temp = int_input(word)
            return temp

numbers = [random.randint(-20,20) for i in range (int_input('длинна массива: '))]
ind =  []
min = int_input('минимальное значение диапозона: ')
max = int_input('максимальное значение диапазона: ')
for i in range (len(numbers)):
     if numbers[i] >= min and numbers[i] <= max:
          ind.append(i)
print(numbers)
print(ind)