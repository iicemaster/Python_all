# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def int_input(word):
        try:
            temp = int(input(word))
            return temp
        except:
            print("Вы ошиблись, попробуйте еще раз")
            temp = int_input(word)
            return temp
        

number = int_input("Введите Первый элемент: ")
interval = int_input("Введите разность: ")
count = int_input("Введите количество элементов: ")
result = list(range(number,(number+interval*count),interval))
print(result)