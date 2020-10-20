words = input("Введите слова с пробелами\n>>>: ")
word = []
length = 1
for k in range(words.count(' ') + 1):
    word = words.split()
    if len(str(word)) <= 10:
        print(f" {length} {word [k]}")
        length += 1
    else:
        print(f" {length} {word [k] [0:10]}")
        length += 1
