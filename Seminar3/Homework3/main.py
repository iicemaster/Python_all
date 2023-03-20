# # *Задача 20: 
# # В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# # В случае с английским алфавитом очки распределяются так:
# # A, E, I, O, U, L, N, S, T, R – 1 очко; 
# # D, G – 2 очка; 
# # B, C, M, P – 3 очка; 
# # F, H, V, W, Y – 4 очка; 
# # K – 5 очков; 
# # J, X – 8 очков; 
# # Q, Z – 10 очков. 
# # А русские буквы оцениваются так: 
# # А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# # Д, К, Л, М, П, У – 2 очка; 
# # Б, Г, Ё, Ь, Я – 3 очка; 
# # Й, Ы – 4 очка; 
# # Ж, З, Х, Ц, Ч – 5 очков; 
# # Ш, Э, Ю – 8 очков; 
# # Ф, Щ, Ъ – 10 очков. 
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# # Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# # *Пример:*
# # ноутбук
# #     12

#Словари
russian = {1: 'а,в,е,и,н,о,р,с,т',
           2: 'д,к,л,м,п,у',
           3: 'б,г,ё,ь,я',
           4: 'й,ы',
           5: 'ж,з,х,ц,ч',
           8: 'ш,э,ю',
           10: 'ф,щ,ъ'}
english = {1: 'a,e,i,o,u,l,n,s,t,r',
           2: 'd,g',
           3: 'b,c,m,p',
           4: 'f,h,v,w,y',
           5: 'k',
           8:  'j,x',
           10: 'q,z'}

#Функция проверки на наличие символов + ограничение в выборе между 0 и 1     
def int_input(word):
    
        try:
            temp = int(input(word))
            if temp == 0 or temp ==1:
                return temp
            else:
                 print("Вы ошиблись, попробуйте еще раз")
                 temp = int_input(word)
                 return temp
        except:
            print("Вы ошиблись, попробуйте еще раз")
            temp = int_input(word)
            return temp

#Функция очистка входящего слова от мусора
def text_input(word):
   result=''
   dict = {1:'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьёбю'}
   temp = input(word)
   temp = [i for i in temp.lower() for key, value in dict.items() if i in value]
   for i in temp: 
       result+=i
   return result

#Рабочая часть кода
lang = int_input('Выберите язык: 0 - Русский, 1 - Английский: ')
text = text_input("Введите слово на русском или английском языке: ")

if lang == 0:
    print('Стоимость слова', text,'на русском языке', '=', sum([key for i in text.lower() for key, value in russian.items() if i in value]))
elif lang == 1:
    print('Стоимость слова', text,'на английском языке','=', sum([key for i in text.lower() for key, value in english.items() if i in value ]))
else:
    print('Вы не выбрали язык, попробуйте еще раз')




