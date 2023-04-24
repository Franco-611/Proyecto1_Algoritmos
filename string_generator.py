import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
strings_num = 10
strings_generadas = []
for i in range(strings_num):
    strings = []
    for i in range(2):
        length = random.choice(numbers)
        string = ""
        for j in range(length):
            string += random.choice(letters)
        strings.append(string)
    strings_generadas.append(strings)

print(strings_generadas)