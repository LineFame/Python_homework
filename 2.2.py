k = int(input("Введите количество индексов\n>>>:  "))
list_1 = []
i = 0
while i < k:
    list_1.append(input("Введите список\n>>>:  "))
    i += 1
print(list_1)
el=0
for i in range(int(len(list_1)/2)):
        list_1[el], list_1[el + 1] = list_1 [el + 1], list_1[el]
        el += 2
print(list_1)
