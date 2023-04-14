# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 
def int_input(word):
        try:
            temp = int(input(word))
            return temp
        except:
            print("Вы ошиблись, попробуйте еще раз")
            temp = int_input(word)
            return temp        
def step(num_a, num_b):
     if num_b > 0:
          num_a += 1
          num_b -= 1
          step(num_a, num_b)
     else :
          print(num_a)
a = int_input("Введите число A: ")
b = int_input("Введите число B: ")
step(a, b)
