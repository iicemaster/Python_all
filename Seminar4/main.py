# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def sorting(list):
    for i in range(len(list)):
        if len(list)-1 > i:
            if list[i] == list[i+1]:
                list.pop(i)
                list = sorting(list)
    return list
num_1 = [int(input('Введите число для 1 набора: ')) for i in range(int(input('Длина набора 1: ')))]
num_2 = [int(input('Введите число для 2 набора: ')) for b in range(int(input('Длина набора 2: ')))]
num_3 = num_1 + num_2
print(sorting(sorted(num_3)))
