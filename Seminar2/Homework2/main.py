# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите(s) сумму x,y: "))
p = int(input("Введите(p) произведение x,y: "))
stop = True

x=1
while stop==True:
    for y in range (1000):
        if (x+y==s) and (x*y==p):
            print(x,y) 
            stop=False  
    x+=1
