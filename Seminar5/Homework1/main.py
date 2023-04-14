# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def int_input(word):
        try:
            temp = int(input(word))
            return temp
        except:
            print("Вы ошиблись, попробуйте еще раз")
            temp = int_input(word)
            return temp
        
def step(num_a, num_b):
     if num_b > 1:
          num_a *= a
          num_b -= 1
          step(num_a, num_b)
     else :
          print(num_a)

a = int_input("Введите число A: ")
b = int_input("Введите число B: ")
step(a, b)