import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

strings_num = 20
strings_generadas = []
for i in range(strings_num):
    strings = []
    length = (i+1) * 10
    for i in range(2):
        string = ""
        for j in range(length):
            string += random.choice(letters)
        strings.append(string)
    strings_generadas.append(strings)

print(strings_generadas)
