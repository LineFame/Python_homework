month = int(input('Введите номер месяца\n>>>: '))
list_seasons = ['Весна',"Лето","Осень","Зима"]

if 2 < month < 6:
    print(list_seasons[0])
elif 5 < month < 9:
    print(list_seasons[1])
elif 8 < month < 12:
    print(list_seasons[2])
elif 11 < month < 13  or 0 < month < 3:
    print(list_seasons[3])

dict_seasons = {1:"Весна", 2:"Лето", 3:"Осень", 4:"Зима"}

if 2 < month < 6:
    print(dict_seasons.get(1))
elif 5 < month < 9:
    print(dict_seasons.get(2))
elif 8 < month < 12:
    print(dict_seasons.get(3))
elif 11 < month < 13  or 0 < month < 3:
    print(dict_seasons.get(4))