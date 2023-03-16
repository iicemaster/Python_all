# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input('Введите трёхзначное число: ')
result = 0
for i in range(len(number)):
    result= result + int(number[i])
print('Сумма цифр трёхзначного числа', number, '=', result)