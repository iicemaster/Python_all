



a = input("Число: ")
count = 1
result = 'true'
for i in range(len(a)):
    try:
        count = count*int(a[i])
        i+=1
    except:
        break
print(count)

while result:
    