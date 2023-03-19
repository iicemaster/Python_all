# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

print('Вариант с последовательными числами в массиве')
n = int(input("Введите количество элементов в массиве: "))
numbers = [i for i  in range(n)]
x = int(input("Введите искомое число: "))
print('Искомое число',x,'встречается', numbers.count(x), 'раз')
# numbers.count(x)
print("")

print('Вариант с случайными числами')
n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите искомое число(от 0 до 10): "))
numbers = [random.randint(0,11) for i in range(n)]
print('Искомое число',x,'встречается', numbers.count(x), 'раз')
print(numbers)